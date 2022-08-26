const sections = document.querySelectorAll('.section');
const sectBtns = document.querySelectorAll('.controlls');
const sectBtn = document.querySelectorAll('.control');
const allSections = document.querySelector('.main-content');

function pageScroll() {
      allSections.addEventListener('click', (e) =>{
            const id = e.target.dataset.id;
            if(id){
                  // remove
                  
                  // hide
                  const element = document.getElementById(id);
                  sections.forEach((section) =>{
                        section.classList.remove('active')
                  })

                  element.classList.add('active');
            }
      })
}

pageScroll()