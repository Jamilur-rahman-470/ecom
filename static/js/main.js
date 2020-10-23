$(document).ready(() => {
    var nav = document.querySelector('#nav-fix')
    window.innerWidth <= 768 ? nav.classList.remove('float-right') : nav.classList.add('float-right')


    // FIX AUTH FORM

    var input_fields = document.querySelectorAll('.auth-group input')
    // console.log(input_fields);
    input_fields[0].placeholder = 'Username'
    input_fields[1].placeholder = 'Email'
    input_fields[2].placeholder = 'Password minmum 8 character'
    input_fields[3].placeholder = 'Confirm Password'
    input_fields.forEach(elm =>{
        elm.classList.add('form-control')
        elm.id = elm.id + ' fix'
    })
})
