function hideByTimer(id, time)
{
    setTimeout(function (){
        $(id).animate({opacity: 0.0}, time/2);
    }, time);
    $(id).css('visibility', 'visible')
}