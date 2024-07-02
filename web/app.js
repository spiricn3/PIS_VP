const BASE_URL = "/api";

function w3_open() {
    document.getElementById("main").style.marginLeft = "25%";
    document.getElementById("mySidebar").style.width = "25%";
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("openNav").style.display = 'none';
}
function w3_close() {
    document.getElementById("main").style.marginLeft = "0%";
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("openNav").style.display = "inline-block";
}


async function getVozila() {
    // popunjavanje tabele

    // selektuje table body iz html-a
    let tableBody = document.getElementById("tableBody")
    tableBody.innerHTML = null // čisti tabelu prije popunjavanja 

    try {
        // kreiramo red u tabeli
        let row
        const response = await fetch(`http://127.0.0.1:8000/api/vozila/`)
        const data = await response.json() // niz svih vozila iz baze

        data.forEach((vozilo) => {
            row = `
            <tr>
                <td>${vozilo?.id}</td>
                <td>${vozilo?.marka}</td>
                <td>${vozilo?.model}</td>
                <td>${vozilo?.registracijski_broj}</td>
                <td>${vozilo?.datum_isteka_registracije}</td>
                <td>${vozilo?.godina_proizvodnje}</td>
                <td>${vozilo?.tip_goriva}</td>
                <td>${vozilo?.status}</td>
                <td><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-pencil" 
                        viewBox="0 0 16 16"
                        onClick="openUpdateModal(${vozilo?.id})"
                        >
                        <path
                            d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325" />
                    </svg></td>
                <td>
                    <div class="action-button" onClick="deleteVozilo(${vozilo?.id})">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-trash" viewBox="0 0 16 16">
                            <path
                                d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z" />
                            <path
                                d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z" />
                        </svg>
                    </div>
                </td>
            </tr>
            `
            tableBody.innerHTML += row

        })

    } catch (err) {
        tableBody.innerHTML = `<tr>Desila se greška!</tr>`
    }
}

async function deleteVozilo(voziloId) {
    console.log("pozvana funkcija")
    try {
        // pokušavamo da izbrišemo vozilo
        const response = await fetch(`http://127.0.0.1:8000/api/vozila/${voziloId}`, {
            method: "DELETE"
        })

        getVozila()

    } catch (err) {
        // ako se desi greška prilikom brisanja odradi ovo ispod
        console.log("greška je", err);
    }
}

getVozila()

async function insertVozilo() {




    const vozilo = {
        marka: document.getElementById("marka").value,
        model: document.getElementById("model").value,
        registracijski_broj: document.getElementById("registracija").value,
        datum_isteka_registracije: document.getElementById("datumRegistracije").value,
        godina_proizvodnje: document.getElementById("godiste").value,
        tip_goriva: document.getElementById("gorivo").value,
        status: document.getElementById("status").value
    }

    try {
        for (let voziloAtribut in vozilo) {
            // for petlja prolazi kroz svaki atribut objekta vozilo
            // if provjerava da li je polje prazno
            if (!vozilo[voziloAtribut]) {
                throw new Error("Nisu popunjena sva polja!")
            }
        }

        // pokušavamo da pošaljemo podatke na server i upišemo u bazu pomoću fetcha
        const response = await fetch(`http://127.0.0.1:8000/api/vozila/`, {
            method: "POST", // metoda post je za slanje podataka tj. upis
            body: JSON.stringify(vozilo), // u body ide objekat koji šaljemo apiju tj vozilo
            headers: {
                "Content-type": "application/json" // tip podatka
            }
        })

        if (!response.ok) { // provjeravamo da li nije upisan podatak u bazu
            throw new Error("Podaci nisu upisani u bazu!") // ako nije bacamo grešku
        }

        // forsira refresh stranice
        location.reload()

    } catch (err) { // hvatamo grešku
        document.getElementById("greskaUpisa").innerHTML = err?.message
    }

}

let idSelektovanogVozila = null

const openUpdateModal = async (idVozila) => {
    // openUpdateModal funkcija otvara modal i popunjava ga sa podacima odabranog vozila

    idSelektovanogVozila = idVozila

    var myModal = new bootstrap.Modal(document.getElementById('updateModal'), {
        keyboard: false
    }) // selektujemo update modal iz DOM-a

    myModal.show()

    try {
        // fetchujemo podatke za vozilo na koje kliknemo upate
        const response = await fetch(`http://127.0.0.1:8000/api/vozila/${idVozila}`)

        if (!response.ok) { // provjeravamo da li nije upisan podatak u bazu
            throw new Error("Ne možemo da dobijemo podatke!") // ako nije bacamo grešku
        }

        const data = await response.json()

        // linije ispod popunjavaju input boxove u update modalu
        document.getElementById("markaUpdate").value = data?.marka
        document.getElementById("modelUpdate").value = data?.model
        document.getElementById("registracijaUpdate").value = data?.registracijski_broj
        document.getElementById("datumRegistracijeUpdate").value = data?.datum_isteka_registracije
        document.getElementById("godisteUpdate").value = data?.godina_proizvodnje
        document.getElementById("gorivoUpdate").value = data?.tip_goriva
        document.getElementById("statusUpdate").value = data?.status
    } catch (err) {
        document.getElementById("greskaUpisaUpdate").innerHTML = err?.message
    }

}

const updateVozilo = async () => {



    // kreiramo veliki objekat koji šaljemo na server
    const vozilo = {
        // isti nazivi atributa kao na backendu
        marka: document.getElementById("markaUpdate").value,
        model: document.getElementById("modelUpdate").value,
        registracijski_broj: document.getElementById("registracijaUpdate").value,
        datum_isteka_registracije: document.getElementById("datumRegistracijeUpdate").value,
        godina_proizvodnje: document.getElementById("godisteUpdate").value,
        tip_goriva: document.getElementById("gorivoUpdate").value,
        status: document.getElementById("statusUpdate").value
    }

    try {
        for (let voziloAtribut in vozilo) {
            // for petlja prolazi kroz svaki atribut objekta vozilo
            // if provjerava da li je polje prazno
            if (!vozilo[voziloAtribut]) {
                throw new Error("Nisu popunjena sva polja!")
            }
        }
        // pokušavamo da pošaljemo podatke na server i izmjenimo u bazi pomoću fetcha
        const response = await fetch(`http://127.0.0.1:8000/api/vozila/${idSelektovanogVozila}`, {
            method: "PUT", // metoda put je za update podataka 
            body: JSON.stringify(vozilo), // u body ide objekat koji šaljemo apiju tj vozilo
            headers: {
                "Content-type": "application/json" // tip podatka
            }
        })

        if (!response.ok) { // provjeravamo da li nije izmjenjen podatak u bazu
            throw new Error("Podaci nisu imjenjeni u bazi!") // ako nije bacamo grešku

        }

        location.reload()  
        
    } catch (err) { // hvatamo grešku
        document.getElementById("greskaUpisaUpdate").innerHTML = err?.message
    }
}

const clearInputFields = () => {
    // ova funkcija čisti input polja, odnosno briše dosadašnji input
    document.getElementById("marka").value = ""
    document.getElementById("model").value = ""
    document.getElementById("registracija").value = ""
    document.getElementById("datumRegistracije").value = ""
    document.getElementById("godiste").value = ""
    document.getElementById("gorivo").value = ""
    document.getElementById("status").value = ""
}

var myModalEl = document.getElementById('exampleModalLabel') // selektujemo insert modal
myModalEl.addEventListener('hidden.bs.modal', function (event) {
    // na zatvaranje insert modala pokrećemo clear inputs funkciju koja čisti input polja
    clearInputFields()
    // kod ispod uklana i prikaz greške kod validacije
    document.getElementById("greskaUpisa").innerHTML = null
})



// nakon dugmeta sačuvaj modal se ne zatvara