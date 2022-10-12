let score = 0;

function showScore(){
  const totalScore = document.getElementById('score-message');
  if(score === 3) {
    totalScore.innerHTML = score + "点：満点！おめでとう！";
  } else if(score === 2) {
    totalScore.innerHTML = score + "点：あともう一息！";
  } else if(score === 1) {
    totalScore.innerHTML = score + "点：まあまあ";
  } else {
    totalScore.innerHTML = score + "点：残念";
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

//cookie
function my_cookie(){
  var cookies = document.cookie; //全てのcookieを取り出して
  var cookiesArray = cookies.split(';'); // ;で分割し配列に

  for(var c of cookiesArray){ //一つ一つ取り出して
      var cArray = c.split('='); //さらに=で分割して配列に
      // if( cArray[0] == 'score'){ // 取り出したいkeyと合致したら
          console.log(cArray);  // [key,value] 
      // }
  }
}
