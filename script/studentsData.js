let studentsInfo = [];

const addStudentData = (e) => {

    e.preventDefault();

    let studentInfo = {
        s_name: document.getElementById('s_name').value,
        dob: document.getElementById('dob').value,
        sex: document.getElementById('sex').value,
        bg: document.getElementById('bg').value,
        gen: document.getElementById('gen').value,
        ail:ailFxn(),
        bp: document.getElementById('bp').value,
        state: document.getElementById('state').value,
        lga: document.getElementById('lga').value,
        school: document.getElementById('school').value,
        school_address: document.getElementById('school_address').value,
        class_: document.getElementById('class_').value,
        year: document.getElementById('year').value,
        siblings:siblingsDataset(),
        pname: document.getElementById('pname').value,
        occupation: document.getElementById('occupation').value,
        raddress: document.getElementById('raddress').value,
        oaddress: document.getElementById('oaddress').value,
        tel: document.getElementById('tel').value,
        Etel: document.getElementById('Etel').value,
        pemail: document.getElementById('pemail').value
    }

    studentsInfo.push(studentInfo);
    document.querySelector('form').reset();

    return JSON.stringify(studentsInfo);
}

function ailFxn() {
    let ailArr = [];
    const clist = document.getElementsByClassName('ail');  
    const clistLen =  document.getElementsByClassName('ail').length; 
      
    for ( let i= 0; i < clistLen ; i++){  
        let  checkedAil = clist[i];                     
        if (checkedAil.checked){  
          ailArr.push(checkedAil.value);  
        }  
    }
    if(document.getElementById('other').value){
        ailArr.push(document.getElementById('other').value);
    }
    
    return ailArr;
}

function siblingsDataset() {

    let siblingsArr = [];
    const numberOfSiblings = document.getElementById('number-of-siblings').value;
    let sibName = document.getElementsByClassName('S_name');
    let sibClass = document.getElementsByClassName('S_class');
    let sibYear = document.getElementsByClassName('S_year'); 

    for(let i = 0; i < numberOfSiblings ;i++){
        let siblingInfo = {
            S_name: sibName[i].value,
            S_class: sibClass[i].value,
            S_year: sibYear[i].value };

        siblingsArr.push(siblingInfo);
    }

   return siblingsArr;

}




document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.btn-submit-form').addEventListener('click', addStudentData);
});