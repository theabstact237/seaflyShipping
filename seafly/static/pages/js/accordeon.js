(function () {
    let menus = document.querySelectorAll(".drawer--menu--item");
    menus.forEach((menu, ielt) => {
        let accordeon = menu.querySelector(".drawer--menu--accordeon");
        if(accordeon !== null){
            let h = accordeon.querySelector('ul').offsetHeight;
            let header = menu.querySelector(".drawer--menu--head");
            header.addEventListener('click',() => {
                if(accordeon.classList.contains('acr' + ielt)){
                    $('.acr' + ielt).animate({
                        height: 0 + 'px',
                    }, 500);
                    accordeon.classList.remove('acr' + ielt)
                } else {
                    accordeon.classList.add("acr" + ielt);
                    $('.acr' + ielt).animate({
                        height: h + 'px',
                    }, 500);
                }
            })
        }
    })
})();
