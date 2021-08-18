


    $(document).ready(function(){
        $(".dropdown").hover(
           
            function(){
                $('.dropdown-menu', this).stop().fadeIn("fast");
               
            },
            function(){
                $('.dropdown-menu', this).stop().fadeOut("fast");
            }
        )
    })
