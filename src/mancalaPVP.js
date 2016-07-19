//Copyright (c) 2016 Qian Song

//This program is available under MIT licence, please see COPYING.

//Javascript code for mancala game

//Term: summer 2016


$(document).ready(function() { 
	newGame();
	
});

//---- Global variables ------
var A = ["Player2", 0, 4, 4, 4, 4, 4, 4];
var B = ["Player1", , 4, 4, 4, 4, 4, 4, 0];
var player;		
var move_again;

//----------- New game -----------		
function newGame() {
	init();	
	if(isEndGame() === false) {
		play();
	}
}

//---------- Start to play ---------
function play() {
		//choose a pit to click to move the stones
		
		$('#B2'). click(function () {
			if(player === 1) {
				move_again = move(1, 2);
				if (!move_again) {
					switchPlayer(1);
					
				}
				if (isEndGame() === true) {
					showResult();	
				}	
			}			
		});
		
		$('#B3'). click(function () {
			
			if(player === 1) {
				move_again = move(1, 3);
				if (!move_again) {
					switchPlayer(1);
					
				}
				if (isEndGame() === true) {
					showResult();	
				}	
			}		
		});
	
		$('#B4'). click(function() {
			if(player === 1) {
				move_again = move(1, 4);
				if (!move_again) {
					switchPlayer(1);
					
				}
				if (isEndGame() === true) {
					showResult();	
				}	
			}		
		});
	
		$('#B5'). click(function () {
			if(player === 1) {
				move_again = move(1, 5);
				if (!move_again) {
					switchPlayer(1);
					
				}
				if (isEndGame() === true) {
					showResult();	
				}	
			}		
			
		});
		$('#B6'). click(function () {
			if(player === 1) {
				move_again = move(1, 6);
				if (!move_again) {
					switchPlayer(1);
					
				}
				if (isEndGame() === true) {
					showResult();	
				}	
			}		
		});
	
		$('#B7'). click(function () {
			if(player === 1) {
				move_again = move(1, 7);
				if (!move_again) {
					switchPlayer(1);
					
				}
				if (isEndGame() === true) {
					showResult();	
				}	
			}		
			
		});
	
		$('#A2'). click(function () {
			if (player === 2) {
				move_again = move(2, 2);
				if (!move_again) {
					switchPlayer(2);
				
				}
				if (isEndGame() === true) {
					showResult();	
				}
			}	
		});
	
		$('#A3'). click(function() {
			if (player === 2) {
				move_again = move(2, 3);
				if (!move_again) {
					switchPlayer(2);
				
				}
				if (isEndGame() === true) {
					showResult();	
				}
			}	
			
		});
		$('#A4'). click(function () {
			if (player === 2) {
				move_again = move(2, 4);
				if (!move_again) {
					switchPlayer(2);
				
				}
				if (isEndGame() === true) {
					showResult();	
				}
			}	
		});
		
		$('#A5'). click(function () {
			if (player === 2) {
				move_again = move(2, 5);
				if (!move_again) {
					switchPlayer(2);
				
				}
				if (isEndGame() === true) {
					showResult();	
				}
			}	
		});
		$('#A6'). click(function () {
			if (player === 2) {
				move_again = move(2, 6);
				if (!move_again) {
					switchPlayer(2);
				
				}
				if (isEndGame() === true) {
					showResult();	
				}
			}		
		});
		$('#A7'). click(function () {
			if (player === 2) {
				move_again = move(2, 7);
				if (!move_again) {
					switchPlayer(2);
				
				}
				if (isEndGame() === true) {
					showResult();	
				}
			}		
		});		
		
}

//------------Prompt Switch to the other player ---------

function switchPlayer(currentPlayer) {
	
	if (currentPlayer === 1) {
		player = 2;
		$('#B0').css("background-color","black");
		$('#A0').css("background-color","red");
		
	} else {
		player = 1;
		$('#B0').css("background-color","red");
		$('#A0').css("background-color","black");
	}	
}

//---------- Init() -------------

function init() {
		//initialize game by clicking the start button
		$('#pvp').click(function() {
				player = 1; //array B
				$(this).css("color", "black");	
                $('#B0').css("background-color","red");
            	$('#promptStart').text("Start playing! Choose a pit to move!") 
			 	
		});
		
		A[1] = 0;
		for (i = 2; i <= 7; i++) {
            	A[i] = 4;
        }
        B[8] = 0;
        for (i = 2; i <= 7; i++) {
                B[i] = 4;
        }
		updateBoard();			
}

//-------------  Update Board  ---------------
//whenever elements in A or B change, call this function

function updateBoard() {
		var i;
		var jqRows = $('#boardTable').find('tr');
		var boardA = jqRows.eq(0).find('td');
		var boardB = jqRows.eq(1).find('td');
		
		$('#A0').text("Player2");
		$('#B0').text("Player1");
			
		for (i =1; i < 8; i++) {
            boardA.eq(i).text(A[i]);
        } 
          
        for (i = 2; i < 9; i++) {
            boardB.eq(i).text(B[i]);
        }
}	
		
//-------------  which pit to add one stone  -----              
//return an array, gives whose board and the index(#of element)           
function add_one(mark, i, player) {
				if (mark === 1) {
					if (i <= A.length - 2) { 
						return [mark, i + 1]; 
					} else if (i === A.length - 1) {
						if (player === 1) {
					 		return [mark, i+1];
					 	} else {
							return [3 - mark, A.length - 1];
						} 
					} else {
						return [3-mark, A.length - 1];
					}
				} else {
						if (i >= 3) { 
							return [mark, i-1]; 
						} else if (i === 2) {
							if (player === 2) {
							 	return [mark, i-1];
							} else {
								return [3-mark, 2];
							}
						} else {
							return [3-mark, 2];
						}
				}

}
//------------ Game Over ---------- 

function gameOver() {
	if(isEndGame() === true) {
		clearGame();
			//game over sign
		if (evaluation() === true) {
			$('#B0').css("background-color","yellow");
			$('#B0').text("WINNER");
		} else {
			$('#A0').css("background-color","yellow");
			$('#A0').text("WINNER");
		}
	}
}
	         
function isEndGame() {
    	var i = 0;
		var a_mark = true;
		var b_mark = true;
		var result;
		for (i = 2; i <= 7; i++) {
			if (A[i] != 0) a_mark = false;
		}
		for (i = 2; i <= 7; i++) {
			if (B[i]!= 0) b_mark = false;
		}
		result = (a_mark || b_mark);
		return result;
} 
	


//--------------- Get the result ---------------
function evaluation() {
		return (B[8] - A[1]);	
}

//-------------- Show who wins --------------------

function showResult() {
		if (evaluation() < 0 ) {
			alert("Winner is: Player2!");
		} else if (evaluation() > 0) {
			alert("Winner is: Player1!");
		} else {
			alert("Ties!");
		}
}	

//--------------- clear the board -----------------------------

function clearGame() {
		var i;
		for (i = 2; i <= 7; i++) {
				A[1] += A[i];
				A[i] = 0;		
		}
		
		for (i = 2; i <= 7; i++) {
				B[8] += B[i];
				B[i] = 0;		
		}
		updateBoard();		
} 

//--------------- Move -------------    

//if current player can continue to move, return true, if not return false
function move(player, i) {
		var sum;
		var mark;
		var position;  
			
		if (player === 1) {
				sum = B[i];
				B[i] = 0;
		} else if (player === 2){
				sum = A[i];
				A[i] = 0;
		}
		//if (sum === 0) {
		//		return false;
		//}
		mark = player;
		while (sum) {
			position = add_one(mark, i ,player);
			mark = position[0];
			i = position[1];
			 		//#of stones in the chosen pit
			 sum = sum - 1;
			if (mark === 1) {
				B[i] += 1;
			}
			else {
				A[i] += 1;
			}
					
		} //end while

		if (isEndGame() === true) {
			clearGame();
			updateBoard();
			return false;
		}
		if (mark != player) {
			updateBoard();
			return false;
		} else {
				if (i === 1 || i === A.length) {
					updateBoard();
					return true;
				}
				if (mark === 1 && B[i] === 1) {
					B[A.length] += B[i] + A[i];
					B[i] = 0;
					A[i] = 0;	
				}
				if (mark === 2 && A[i] === 1) {
					A[1] += A[i] + B[i];
					A[i] = 0;
					B[i] = 0;	
				}
				if (isEndGame() === true) {
					clearGame();
				}
				updateBoard();
				return false;
		}//end else
					
}//end function move
	

