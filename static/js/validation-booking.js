$(document).ready(function(){

    $('#send_message').click(function(e){
        
        e.preventDefault();

        var error = false;

        // Ambil semua field
        var name    = $('#name').val();
        var email   = $('#email').val();
        var phone   = $('#phone').val();
        var message = $('#message').val();
        var service = $('#service').val();
        var date    = $('#date').val();
        var time    = $('#time').val();

        // Remove error saat klik
        $('#name,#email,#phone,#message,#service,#date,#time').on('click', function(){
            $(this).removeClass("error_input");
        });

        // VALIDASI
        if(name.length == 0){
            error = true;
            $('#name').addClass("error_input");
        }

        if(email.length == 0 || email.indexOf('@') == -1){
            error = true;
            $('#email').addClass("error_input");
        }

        if(phone.length == 0){
            error = true;
            $('#phone').addClass("error_input");
        }

        if(message.length == 0){
            error = true;
            $('#message').addClass("error_input");
        }

        if(service.length == 0){
            error = true;
            $('#service').addClass("error_input");
        }

        if(date.length == 0){
            error = true;
            $('#date').addClass("error_input");
        }

        if(time.length == 0){
            error = true;
            $('#time').addClass("error_input");
        }

        // KIRIM AJAX
        if(error == false){

            $('#send_message').attr({'disabled': true, 'value': 'Sending...'});

            $.post("booking.php", {
                name: name,
                email: email,
                phone: phone,
                message: message,
                service: service,
                date: date,
                time: time
            }, function(result){

                if(result == 'sent'){
                    $('#booking_form').fadeOut(300, function(){
                        $('#success_message_col').fadeIn(500);
                    });
                } else {
                    $('#mail_fail').fadeIn(500);
                    $('#send_message').removeAttr('disabled').val('Send The Message');
                }

            });

        }

    });

});