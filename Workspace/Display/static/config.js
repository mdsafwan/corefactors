/**
 * @license Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
//	 config.uiColor = '#1919BD';
	config.width = 500
	config.height = 100
	//config.allowedContent = 'u em strong ul li;a[!href,target]';
	//config.removePlugins = 'image,table,tabletools,horizontalrule';
	//config.removePlugins = 'colorbutton,find,flash,font,' +
	//					'forms,iframe,image,newpage,removeformat,' +
	//					'smiley,specialchar,stylescombo,templates';
	//config.removeButtons = 'Anchor,Underline,Strike,Subscript,Superscript';
	config.toolbar = [
   ['Styles','Format','Font','FontSize'],
   '/',
   ['Bold','Italic','Underline','StrikeThrough','-','Undo','Redo','-','Cut','Copy','Paste','Find','Replace','-','Outdent','Indent','-','Print'],
   '/',
   ['NumberedList','BulletedList','-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
   ['Image','Table','-','Link','Flash','Smiley','TextColor','BGColor','Source']
] ;
	//config.toolbarGroups = [
	//					{ name: 'editing',		groups: [ 'basicstyles', 'links' ] },
	//					{ name: 'undo' },
	//					{ name: 'clipboard',	groups: [ 'selection', 'clipboard' ] },
	//					{ name: 'about' }
	//					];

	config.filebrowserBrowseUrl = '../kcfinder/browse.php?opener=ckeditor&type=files';
   config.filebrowserImageBrowseUrl = '../kcfinder/browse.php?opener=ckeditor&type=images';
   config.filebrowserFlashBrowseUrl = '../kcfinder/browse.php?opener=ckeditor&type=flash';
   config.filebrowserUploadUrl = '../kcfinder/upload.php?opener=ckeditor&type=files';
   config.filebrowserImageUploadUrl = '../kcfinder/upload.php?opener=ckeditor&type=images';
   config.filebrowserFlashUploadUrl = '../kcfinder/upload.php?opener=ckeditor&type=flash';	
};
