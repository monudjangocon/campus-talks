$(function(){
	$('.single_user').click(function(){
		$('.msg_box').show();
	});

	$('.close').click(function(){
      $('.msg_box').hide();
	});

	$('.msg_head').click(function(){
        $('.msg_cover').toggle();
	});

	$('textarea').keypress(function(e){
       if(e.keyCode==13){
       	 var msg=$(this).val();
       	 $('msg_body').append('<br>');
       	 $('.msg_body').html(msg);
       }
	});
	

});