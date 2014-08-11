var PanelOneGate=0;
var PanelTwoGate=0;
var PanelThreeGate=0;
var allTime=250;
var count=0;
function handleAnswerBtn(){

}
function handlePanelTwoGateBtn(){
	count = 0;
    $('.timer').css({'display':'block'}).animate({'opacity':1,'right':0});
    var timer = $.timer(
        function() {
            count++;
             $('.timer .time').html(allTime-count);
             if(count==allTime){
                count=0;
             	$('.fancybox-overlay').click()
                $('.timer .time').html('');
                $('.timer').animate({'right':-150,'opacity':0}).css({'display':'none'});
             }
        },
            1000,
            true
          );  
}
$(document).ready(function(){
	$('.gateTwoBtn').click(function(){
		handlePanelTwoGateBtn();
	});
    $('.closeTimer').click(function(){
        count=0;
        $('.timer .time').html('');
        $('.timer').animate({'right':-150,'opacity':0}).css({'display':'none'});
    });
});