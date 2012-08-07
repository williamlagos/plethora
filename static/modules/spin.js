/* Namespace Spin */ spin = {

createHelix:function(){
	$('#efforia').drawSVG('interface.svg',$.e.h-40,$.e.h-40);
	$.e.widthNow = $('body').width();	
},

holdHelix:function(event){
	event.preventDefault();
	$.e.holding = true; $.e.clicked = true; 
},

releaseHelix:function(event){
	event.preventDefault(); 
	$.e.holding = false;
	$.e.value = true; 
	if(!$.e.clicked){
		$.e.marginTop += margin;
		$.e.marginMax = -$('.mosaic-block').height()*$.e.marginFactor;
		$('#Grade').translate(0,$.e.marginTop);
		if($.e.marginTop > 0 && margin > 0){
			$('#Grade').translate(0,$.e.marginTop); $.e.marginTop = 0;
			setTimeout(function(){$('#Grade').translate(0,$.e.marginTop);},1000);
		}else if($.e.marginMax-$.e.marginTop > 0 && margin < 0){
			$('#Grade').translate(0,$.e.marginTop); $.e.marginTop = $.e.marginMax;
			setTimeout(function(){$('#Grade').translate(0,$.e.marginTop);},1000);
		}
		setTimeout(function(){ $.e.angle = 0; $('#efforia').rotate($.e.angle);},1000);
	}
	if (!$.e.holding && $.e.clicked && $.e.value) {
		$.fn.hideMenus();
	}
},

moveHelix:function(event){
	event.preventDefault();
	if ($.e.holding) {
		$.e.clicked = false;
		x = event.pageX; y = event.pageY;
		if ($.e.velocity < 0) $.e.velocity = -$.e.velocity;
		// Sentido antihorario
		if ($.e.velocity >= $.e.last) {
			margin = -$('.mosaic-block').height()*2;
			$.e.last = $.e.velocity;
			$.e.velocity = -(Math.atan(y/x))*$.e.acceleration;
		// Sentido horario
		} else if ($.e.velocity < $.e.last) {
			margin = $('.mosaic-block').height()*2;
			$.e.last = $.e.velocity;
			$.e.velocity = Math.atan(y/x)*$.e.acceleration;
		}
		$.e.angle += $.e.velocity;
		$('#efforia').rotate($.e.angle);
	}
},

resizeHelix:function(event){
	heightBefore = $.e.h;
	$.e.w = window.innerWidth*0.85;
	$.e.h = window.innerHeight-40;
	$.e.widthNow = $('body').width();
	$('#Canvas').css({height:$.e.h,width:$.e.w});
	$('#efforia').scale($.e.h/heightBefore);
	if($.e.widthNow < 1280) $('body').css({'font-size':'0.8em'});
	else if($.e.widthNow > 1280) $('body').css({'font-size':'1.0em'});
}

}