window.onload = function(){
    var hw = document.getElementById('hw');
    hw.addEventListener('click', function(){
        alert('휴지통으로 이동됩니다.');
    })
}
window.onload = function(){

    $(document).on('click', '.confirm-delete', function(){
        return confirm('정말로 지우시겠습니까?');
    })

}
