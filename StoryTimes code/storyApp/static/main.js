// bootstrap tolltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));

// bootstrap Toasts

const toastElList = document.querySelector('.toast');
if(toastElList){
    const toast = new bootstrap.Toast(toastElList);
    toast.show()
}


// bootstrap modals

const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')
if(myModal){
    myModal.addEventListener('shown.bs.modal', () => {
    myInput.focus()
    })
}

console.log(true)

















