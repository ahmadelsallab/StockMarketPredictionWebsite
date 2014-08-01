<?php
	class Tweet extends Eloquent {
		 public static $table = 'tweets';
		 public static $timestamps='true';

		 // public function validate($inputCode){
		 // 	if((Code::where('value','=',$inputCode)->first())!= NULL){
		 // 		return true;
		 // 	}
		 // }

		 // public function questions(){
		 // 	return $this->has_many_and_belongs_to('Question');
		 // }
	}
?>