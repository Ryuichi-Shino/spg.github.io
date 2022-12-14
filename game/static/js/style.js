let score = 0;

function showScore(){
  const totalScore = document.getElementById('score-message');
  if(score === 10) {
    totalScore.innerHTML = score + "点：満点！おめでとう！";
  } else if(score >= 7) {
    totalScore.innerHTML = score + "点：あともう一息！";
  } else if(score >= 4) {
    totalScore.innerHTML = score + "点：まだまだ";
  } else {
    totalScore.innerHTML = score + "点：もっとがんばろう";
  }   
}

const correct = '正解です';
const incorrect = '不正解です';

function answerQuiz1() {
  const quiz_1 = document.getElementById('quiz-1');
  const select = "1問目:" + quiz_1.answer.value + 'を選択しました';
  if (quiz_1.answer.value == 'a') {
    score++;
    console.log(select);
    console.log(correct);
  } else if (quiz_1.answer.value == 'b') {
    console.log(select);
    console.log(incorrect);
  } else if (quiz_1.answer.value == 'c') {
    console.log(select);
    console.log(incorrect);
  } else {
    alert('1問目の答えを入力してください');
  }
  console.log('現在の点数：' + score); 
}

function audio() {
  document.getElementById('btn_audio').currentTime = 0; //連続クリックに対応
  document.getElementById('btn_audio').play(); //クリックしたら音を再生
}

function delay() {
  setTimeout(function() {
    target.innerText = "ボタンがクリックされました。";
  }, 2000);
}

const bgm = document.querySelector('bgm_audio');

function bgm() {
  if(! bgm.paused){
    bgm.paused();
  }
  else{
    bgm.play();
  }
}

function audio() {
  document.getElementById('btn_audio').currentTime = 0; //連続クリックに対応
  document.getElementById('btn_audio').play(); //クリックしたら音を再生
}