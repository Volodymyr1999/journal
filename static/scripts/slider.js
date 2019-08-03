$(function () {
    items=$('.les-item');
    left = 0;
    for(var i=0;i<items.length;i++){

        items[i].style.left = left+'px';
        left+=items.eq(i).width()
    }
    $('.les-item').first().addClass('current');


});
function change(value) {

        $('.les-item').animate({'left':'+=valuepx'.replace('value',value)},500);
    }
function changeRight() {

    left = -$('.current').width();
    index = $('.current').index();

    if(index == $('.les-item').last().index()){
        return false;
    }

    $('.les-item').eq(index).removeClass('current');
    if(index!=$('.les-item').last().index()){
        $('.les-item').eq(index+1).addClass('current');
    }



    change(left)

}
function changeLeft() {

    right = $('.current').width();
    index = $('.current').index();
    if(index == $('.les-item').first().index()){
        return false;
    }

    $('.les-item').eq(index).removeClass('current');
    if(index!=$('.les-item').first().index()){
        $('.les-item').eq(index-1).addClass('current');
    }


    change(right);
}