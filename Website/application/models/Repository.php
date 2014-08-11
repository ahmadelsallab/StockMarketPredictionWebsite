<?php
class Repository extends Eloquent {
	public static $table = 'repositories';
	
	public function get_title(){
		if(Config::get('application.language')==='ar'){
			return $this->get_attribute('title');
		}
		else{
			return $this->get_attribute('title_en');
		}
	}
}

?>