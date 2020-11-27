/**
Company : Dazzler Software Pvt. Ltd
File 	: custom.js
Version	: 1.0 
**/
var ZESTO = function(){
	/* Main Search Bar ============ */
	websitePath = '';
	
	var screenWidthVar = $( window ).width();
	
	var mainSearch = function() {
		'use strict';
		/* main search in header on click function */
		var quikSearch = jQuery("#daz-search-btn");
		var quikSearchRemove = jQuery("#daz-search-remove");
		
		quikSearch.on('click',function() {
			jQuery('.daz-search').fadeIn(500);
			jQuery('.daz-search').addClass('On');
		});
		quikSearchRemove.on('click',function() {
			jQuery('.daz-search').fadeOut(500);
			jQuery('.daz-search').removeClass('On');
		});	
		/* main search in header on click function End*/
	}
	
	/* One Page Layout ============ */
	var dazOnePageLayout = function() {
		'use strict';
		var headerHeight =   parseInt($('.onepage').css('height'), 10);
		$(".scroll").unbind().on('click',function(event) 
		{
			event.preventDefault();
			
			if (this.hash !== "") {
				var hash = this.hash;	
				var seactionPosition = $(hash).offset().top;
				var headerHeight =   parseInt($('.onepage').css('height'), 10);
				
				
				$('body').scrollspy({target: ".navbar", offset: headerHeight+2}); 
				
				var scrollTopPosition = seactionPosition - (headerHeight);
				
				$('html, body').animate({
					scrollTop: scrollTopPosition
				}, 800, function(){
					
				});
			}   
		});
		$('body').scrollspy({target: ".navbar", offset: headerHeight + 2});  
	}
	
	/* Header Height ============ */
	var manageResizeElement = function(){
		var headerHeight = $('.header').height();
		$('.header').css('height', headerHeight);
	}
	
	/* Theme Loading Files ============ */
	var dazTheme = function(){
		 'use strict';
		 var loadingImage = '<img src="images/loading.gif">';
		 jQuery('.dzload').each(function(){
		 var dazsrc =   websitePath + $(this).attr('dzsrc');
		  //jQuery(this).html(loadingImage);
		 	jQuery(this).hide(function(){
				jQuery(this).load(dazsrc, function(){
					jQuery(this).fadeIn('slow');
				}); 
			})
			
		 });
		 
		 if(screenWidthVar < 991){
			var logoData = jQuery('<div>').append($('.mobile-nav .daz-logo').clone()).html();
			jQuery('.mobile-nav .header-nav').prepend(logoData);
			jQuery('.mobile-nav .header-nav .daz-logo > a > img').attr('src','images/logo.png');
			jQuery('.mobile-nav.lw .header-nav .daz-logo > a > img').attr('src','images/logo-white.png');
		}
	}
	
	/* Magnific Popup ============ */
	var dazMagnificPopup = function(){
		'use strict';	
		/* dazMagnificPopup function */
		jQuery('.mfp-gallery').magnificPopup({
			delegate: '.mfp-link',
			type: 'image',
			tLoading: 'Loading image #%curr%...',
			mainClass: 'mfp-img-mobile',
			gallery: {
				enabled: true,
				navigateByImgClick: true,
				preload: [0,1] // Will preload 0 - before current, and 1 after the current image
			},
			image: {
				tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
				titleSrc: function(item) {
					return item.el.attr('title') + '<small></small>';
				}
			}
		});
		/* magnificPopup function end */
		
		/* magnificPopup for paly video function */		
		jQuery('.video').magnificPopup({
			type: 'iframe',
			iframe: {
				markup: '<div class="mfp-iframe-scaler">'+
						 '<div class="mfp-close"></div>'+
						 '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>'+
						 '<div class="mfp-title">Some caption</div>'+
						 '</div>'
			},
			callbacks: {
				markupParse: function(template, values, item) {
					values.title = item.el.attr('title');
				}
			}
		});
		/* magnificPopup for paly video function end*/
		$('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
			disableOn: 700,
			type: 'iframe',
			mainClass: 'mfp-fade',
			removalDelay: 160,
			preloader: false,

			fixedContentPos: false
		});
	}
	
	
	/* Scroll To Top ============ */
	var dazScrollTop = function (){
		'use strict';
		var scrollTop = jQuery("button.scroltop");
		/* page scroll top on click function */	
		scrollTop.on('click',function() {
			jQuery("html, body").animate({
				scrollTop: 0
			}, 1000);
			return false;
		})

		jQuery(window).bind("scroll", function() {
			var scroll = jQuery(window).scrollTop();
			if (scroll > 900) {
				jQuery("button.scroltop").fadeIn(1000);
			} else {
				jQuery("button.scroltop").fadeOut(1000);
			}
		});
		/* page scroll top on click function end*/
	}
	
	/* manage Accordian ============ */
	var manageAccordian = function(){
		/* accodin open close icon change */	 	
		jQuery('#accordion').on('hidden.bs.collapse', function(e){
			jQuery(e.target)
				.prev('.panel-heading')
				.find("i.indicator")
				.toggleClass('glyphicon-minus glyphicon-plus');
		});
		jQuery('#accordion').on('shown.bs.collapse', function(e){
			jQuery(e.target)
				.prev('.panel-heading')
				.find("i.indicator")
				.toggleClass('glyphicon-minus glyphicon-plus');
		});
		/* accodin open close icon change end */
	}
	
	/* manage Placeholder ============ */
	var managePlaceholder = function(){
		/* input placeholder for ie9 & ie8 & ie7 browser*/
		jQuery.support.placeholder = ('placeholder' in document.createElement('input'));
		/* input placeholder for ie9 & ie8 & ie7 end*/
		
		/*fix for IE7 and IE8 browser */
		if (!jQuery.support.placeholder) {
			jQuery("[placeholder]").focus(function () {
				if (jQuery(this).val() == jQuery(this).attr("placeholder")) jQuery(this).val("");
			}).blur(function () {
				if (jQuery(this).val() == "") jQuery(this).val(jQuery(this).attr("placeholder"));
			}).blur();

			jQuery("[placeholder]").parents("form").submit(function () {
				jQuery(this).find('[placeholder]').each(function() {
					if (jQuery(this).val() == jQuery(this).attr("placeholder")) {
						 jQuery(this).val("");
					}
				});
			});
		}
		/*fix for IE7 and IE8 end */
	}
	
	/* Equal Height ============ */
	var dazEqualHeight = function(container) {
		
		if(jQuery(container).length == 0)
		{
			return false
		}
			
		var currentTallest = 0, 
			currentRowStart = 0, 
			rowDivs = new Array(), 
			$el, topPosition = 0;
			
		$(container).each(function() {
			$el = $(this);
			$($el).height('auto')
			topPostion = $el.position().top;

			if (currentRowStart != topPostion) {
				for (currentDiv = 0; currentDiv < rowDivs.length; currentDiv++) {
					rowDivs[currentDiv].height(currentTallest);
				}
				rowDivs.length = 0; // empty the array
				currentRowStart = topPostion;
				currentTallest = $el.height();
				rowDivs.push($el);
			} else {
				rowDivs.push($el);
				currentTallest = (currentTallest < $el.height()) ? ($el.height()) : (currentTallest);
			}
			for (currentDiv = 0; currentDiv < rowDivs.length; currentDiv++) {
				rowDivs[currentDiv].height(currentTallest);
			}
		});
		
		
		/*
		
		var currentTallest = 0, 
			currentRowStart = 0, 
			rowDivs = new Array(), 
			$el, topPosition = 0;
			
		$(container).each(function() {
			$el = $(this);
			$($el).height('auto')
			topPostion = $el.position().top;

			if (currentRowStart != topPostion) {
				for (currentDiv = 0; currentDiv < rowDivs.length; currentDiv++) {
					rowDivs[currentDiv].height(currentTallest);
				}
				rowDivs.length = 0; // empty the array
				currentRowStart = topPostion;
				currentTallest = $el.height();
				rowDivs.push($el);
			} else {
				rowDivs.push($el);
				currentTallest = (currentTallest < $el.height()) ? ($el.height()) : (currentTallest);
			}
			for (currentDiv = 0; currentDiv < rowDivs.length; currentDiv++) {
				rowDivs[currentDiv].height(currentTallest);
			}
		});
		
		*/
	}
	
	/* Footer Align ============ */
	var dazFooterAlign = function() {
		'use strict';
		jQuery('.daz-footer').css('display', 'block');
		jQuery('.daz-footer').css('height', 'auto');
		var footerHeight = jQuery('.daz-footer').outerHeight();
		jQuery('.footer-fixed > .page-wraper').css('padding-bottom', footerHeight);
		jQuery('.daz-footer').css('height', footerHeight);
	}
	
		
	/* Header Fixed ============ */
	var dazHeaderFix = function(){
		'use strict';
		/* Main navigation fixed on top  when scroll down function custom */		
		jQuery(window).bind('scroll', function () {
			if(jQuery('.header-sticky').length)
			{
				var menu = jQuery('.header-sticky');
				if ($(window).scrollTop() > menu.offset().top) {
					menu.addClass('is-fixed');
				} else {
					menu.removeClass('is-fixed');
				}
			}
		});
		/* Main navigation fixed on top  when scroll down function custom end*/
	}
	
	/* Masonry Box ============ */
	var dazMasonryBox = function(){
		'use strict';
		
		if(jQuery('#masonry, .masonry').length)
		{
			var self = $("#masonry, .masonry");
			if(jQuery('.card-container').length)
		    {
				self.imagesLoaded(function () {
					self.masonry({
						gutterWidth: 15,
						isAnimated: true,
						itemSelector: ".card-container"
					});
				});
			}
		}
		if(jQuery('.filters').length)
		{
			jQuery(".filters").on('click','li',function(e) {
				e.preventDefault();
				var filter = $(this).attr("data-filter");
				self.masonryFilter({
					filter: function () {
						if (!filter) return true;
						//return $(this).attr("data-filter") == filter;
						return $(this).hasClass(filter);
					}
				});
			});
		}
		
	}
	
		
	/* Set Div Height ============ */
	var dazSetDivHeight = function(){	
		'use strict';
		var allHeights = [];
		jQuery('.dazseth > div, .dazseth .img-cover, .dazseth .seth').each(function(e){
			allHeights.push(jQuery(this).height());
		})

		jQuery('.dazseth > div, .dazseth .img-cover, .dazseth .seth').each(function(e){
			var maxHeight = Math.max.apply(Math,allHeights);
			jQuery(this).css('height',maxHeight);
		})
		
		allHeights = [];
		/* Removice */
		//var screenWidthVar = $( window ).width();
		if(screenWidthVar < 991)
		{
			jQuery('.dazseth > div, .dazseth .img-cover, .dazseth .seth').each(function(e){
				jQuery(this).css('height','');
			})
		}	
	}
	
	/* Counter Number ============ */
	var dazCounter = function(){
		 if(jQuery('.counter').length)
		{
			jQuery('.counter').counterUp({
				delay: 10,
				time: 3000
			});	
		} 
	}
	
	/* Video Popup ============ */
	var manageVideo = function(){
		/* Video responsive function */	
		jQuery('iframe[src*="youtube.com"]').wrap('<div class="embed-responsive embed-responsive-16by9"></div>');
		jQuery('iframe[src*="vimeo.com"]').wrap('<div class="embed-responsive embed-responsive-16by9"></div>');	
		/* Video responsive function end */
	}
	
	/* Gallery Filter ============ */
	var manageFilterMasonary = function(){
		/* gallery filter activation = jquery.mixitup.min.js */ 
		if (jQuery('#image-gallery-mix').length) {
			jQuery('.gallery-filter').find('li').each(function () {
				$(this).addClass('filter');
			});
			jQuery('#image-gallery-mix').mixItUp();
		};
		if(jQuery('.gallery-filter.masonary').length){
			jQuery('.gallery-filter.masonary').on('click','span', function(){
				var selector = $(this).parent().attr('data-filter');
				jQuery('.gallery-filter.masonary span').parent().removeClass('active');
				jQuery(this).parent().addClass('active');
				jQuery('#image-gallery-isotope').isotope({ filter: selector });
				return false;
			});
		}
		/* gallery filter activation = jquery.mixitup.min.js */
	}
	
	/* manage Bootstrap Select ============ */
	var manageBootstrapSelect = function(){
		/* Bootstrap Select box function by  = bootstrap-select.min.js */ 
		if (jQuery('select').length) {
		    jQuery('select').selectpicker();
		}
		/* Bootstrap Select box function by  = bootstrap-select.min.js end*/
	}
	
	/* manage Bootstrap Touch Spin ============ */
	var manageBootstrapTouchSpin = function(){
		jQuery("input[name='demo_vertical2']").TouchSpin({
		  verticalbuttons: true,
		  verticalupclass: 'ti-plus',
		  verticaldownclass: 'ti-minus'
		});
		
	}
	/* Resizebanner ============ */
	var manageBannerResize = function(){
		$(".full-height").css("height", $(window).height());
	}
	
	/* Content Scroll ============ */
	var manageCustomScroll = function(){
		/* all available option parameters with their default values */
		if($(".content-scroll").length)
		{ 
			$(".content-scroll").mCustomScrollbar({
				setWidth:false,
				setHeight:false,
				axis:"y"
			});	
		}
	}
	
	/* WOW ANIMATION ============ */
	var dazWowAnimation = function(){
		if($('.wow').length > 0)
		{
			var wow = new WOW(
			{
			  boxClass:     'wow',      // animated element css class (default is wow)
			  animateClass: 'animated', // animation css class (default is animated)
			  offset:       50,          // distance to the element when triggering the animation (default is 0)
			  mobile:       false       // trigger animations on mobile devices (true is default)
			});
			wow.init();	
		}	
	}
	
	/* Left Menu ============ */
	var manageSideBarMenu = function(){
		$('.openbtn').on('click',function(e){
			e.preventDefault();
			if($('#mySidenav').length > 0)
			{
				document.getElementById("mySidenav").style.left = "0";
			}

			if($('#mySidenav1').length > 0)
			{
				document.getElementById("mySidenav1").style.right = "0";
			}
			
		})
		
		$('.closebtn').on('click',function(e){
			e.preventDefault();
			if($('#mySidenav').length > 0)
			{
				document.getElementById("mySidenav").style.left = "-300px";
			}
			
			if($('#mySidenav1').length > 0)
			{
				document.getElementById("mySidenav1").style.right = "-820px";
			}
		})
	}
	
	
	/* BACKGROUND EFFECT ============ */
	var manageBGElements = function(){
		
		if(screenWidthVar > 1023)
		{
			if(jQuery('.bgeffect').length)
			{
				var s = skrollr.init({
					edgeStrategy: 'set',
					easing: {
						WTF: Math.random,
						inverted: function(p) {
							return 1-p;
						}
					}
				});			
			}		
		}
	}
	
	var dazBoxHover = function(){
	
		jQuery('.box-hover').on('mouseenter',function(){
			jQuery('.box-hover').removeClass('active');
			jQuery(this).addClass('active');
			
		})
	}
	
	var reposition = function (){
		'use strict';
		var modal = jQuery(this),
		dialog = modal.find('.modal-dialog');
		modal.css('display', 'block');
		
		/* Dividing by two centers the modal exactly, but dividing by three 
		 or four works better for larger screens.  */
		dialog.css("margin-top", Math.max(0, (jQuery(window).height() - dialog.height()) / 2));
	}
	
	var manageResize = function (){
		
		/* Reposition when the window is resized */
		jQuery(window).on('resize', function() {
			jQuery('.modal:visible').each(reposition);
			if(jQuery('.equal-wraper').length){
				dazEqualHeight('.equal-wraper .equal-col');
			}
			dazFooterAlign();
		});
	}
	
	
	/* Function ============ */
	return {
		init:function(){
			dazBoxHover();
			//dazWowAnimation();
			dazOnePageLayout();
			dazTheme();
			manageResizeElement();
			mainSearch();
			dazMagnificPopup();
			manageAccordian();
			dazScrollTop();
			managePlaceholder();
			dazFooterAlign();
			dazHeaderFix();
			dazSetDivHeight();
			manageVideo();
			manageCustomScroll();
			manageSideBarMenu();
			manageBannerResize();
			jQuery('.modal').on('show.bs.modal', reposition);
		},
		
		load:function(){
			manageBGElements();
			manageBootstrapSelect();
			manageBootstrapTouchSpin();
			manageResize();
			dazEqualHeight('.equal-wraper .equal-col');
			dazCounter();
			dazMasonryBox();
		}
	}
	
}();

/* Jquery ready Start */	
jQuery(document).ready(function() {
  
	ZESTO.init();
	
	 var screenWidthVar = jQuery( window ).width();
	if(screenWidthVar <= 991 )
	{
		jQuery('.navbar-nav > li > a, .sub-menu > li > a').on('click', function(e){
			//e.preventDefault();
			if(jQuery(this).parent().hasClass('open'))
			{
				jQuery(this).parent().removeClass('open');
			}
			else{
				jQuery(this).parent().parent().find('li').removeClass('open');
				jQuery(this).parent().addClass('open');
			}
		});
		
	}

	jQuery('.menuicon').on('click',function(){
		$(this).toggleClass('open');
	}); 
});
/* Jquery ready END */

/* Window Load START */
$(window).on("load", function (e) {
	ZESTO.load();
	setTimeout(function(){
		jQuery('#loading-area').remove();
	}, 0);
});


/*  Window Load END */