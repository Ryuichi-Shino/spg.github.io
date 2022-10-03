var count = 0

function count(){
    count =+ 1
    return count
  }

function result(){
    return count
}

//sound//
function audio() {
  document.getElementById('btn_audio').currentTime = 0; //連続クリックに対応
  document.getElementById('btn_audio').play(); //クリックしたら音を再生
}