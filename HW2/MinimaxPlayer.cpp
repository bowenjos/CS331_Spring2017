/*
 * MinimaxPlayer.cpp
 *
 *  Created on: Apr 17, 2015
 *      Author: wong
 */
#include <iostream>
#include <assert.h>
#include "MinimaxPlayer.h"

using std::vector;

MinimaxPlayer::MinimaxPlayer(char symb) :
		Player(symb) {

}

MinimaxPlayer::~MinimaxPlayer() {

}

char MinimaxPlayer::get_other_symbol(char symbol){
	if(symbol == 'X'){
		return 'O';
	}else{
		return 'X';
	}
}

int MinimaxPlayer::utility(OthelloBoard* cb) {

	int util = cb->count_score(this->get_symbol()) - cb->count_score(get_other_symbol(this->get_symbol()));
	return util;
}

int MinimaxPlayer::max(OthelloBoard* cb, int c, int r){

	int val;
	int curMax = -99;
	int temp;
	OthelloBoard* copy = new OthelloBoard(*cb);

	copy->play_move(c, r, this->get_other_symbol(this->get_symbol()));
	
	if(!copy->has_legal_moves_remaining(this->get_symbol())){
		val = utility(copy);
		return val;
	}

	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(copy->is_legal_move(i, j, this->get_symbol())){
				temp = min(copy, i, j);
				if(temp > curMax){
					curMax = temp;
				}
			}
		}
	}

	val = curMax;

	return val;
}

int MinimaxPlayer::min(OthelloBoard* cb, int c, int r){

	int val;
	int curMin = 99;
	int temp;
	OthelloBoard* copy = new OthelloBoard(*cb);

	copy->play_move(c, r, this->get_symbol());
	
	if(!copy->has_legal_moves_remaining(this->get_other_symbol(this->get_symbol()))){
		val = utility(copy);
		return val;
	}

	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(copy->is_legal_move(i, j, this->get_other_symbol(this->get_symbol()))){
				temp = max(copy, i, j);
				if(temp < curMin){
					curMin = temp;
				}
			}
		}
	}

	val = curMin;

	return val;
}

mima MinimaxPlayer::firstMax(OthelloBoard* b){
	
	mima temp;
	int val;
	int curMax = 0;
	
	OthelloBoard* copy = new OthelloBoard(*b);

	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(copy->is_legal_move(i, j, this->get_symbol())){
				temp.val = min(copy, i, j);
				if(temp.val > curMax){
					curMax = temp.val;
					temp.c = i;
					temp.r = j;
				}
			}
		}
	}
	temp.val = curMax;

	return temp;
}	

void MinimaxPlayer::get_move(OthelloBoard* b, int& col, int& row) {
    // To be filled in by youi
	
	mima temp;

	temp = firstMax(b);

	std::cout << "c: " << temp.c << std::endl;
	std::cout << "r: " << temp.r << std::endl;	
	col = temp.c;
	row = temp.r;

	return;
	
}

MinimaxPlayer* MinimaxPlayer::clone() {
	MinimaxPlayer* result = new MinimaxPlayer(symbol);
	return result;
}
