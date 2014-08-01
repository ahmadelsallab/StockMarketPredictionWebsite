<?php
	class language_Controller extends Base_Controller {
		public function action_en()
		{
				// Config::set('application.language','en');
				Cookie::forever('language','en');
				return Redirect::to('home/index');
		}
		public function action_ar()
		{
				// Config::set('application.language','ar');
				Cookie::forever('language','ar');
				return Redirect::to('home/index');
		}
	}
?>