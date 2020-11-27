/* JavaScript Document */
jQuery(document).ready(function() {
    'use strict';
	
	/*  Blog post Carousel function by = owl.carousel.js */
	jQuery('.blog-carousel').owlCarousel({
		loop:true,
		autoplay:true,
		margin:30,
		nav:true,
		dots: false,
		navText: ['<i class="flaticon-left-arrow"></i>', '<i class="flaticon-right-arrow"></i>'],
		responsive:{
			0:{
				items:1
			},
			480:{
				items:2
			},			
			991:{
				items:2
			},
			1000:{
				items:3
			}
		}
	})	
		
	/*  testimonial one function by = owl.carousel.js */
	jQuery('.testimonial-one').owlCarousel({
		loop:true,
		autoplay:true,
		margin:30,
		nav:true,
		dots: true,
		navText: ['<i class="ti-arrow-left"></i>', '<i class="ti-arrow-right"></i>'],
		responsive:{
			0:{
				items:1
			},
			
			480:{
				items:1
			},			
			
			767:{
				items:1
			},
			1000:{
				items:1
			}
		}
	})	
	
	/* testimonial two function by = owl.carousel.js */
	jQuery('.testimonial-center').owlCarousel({
		center: true,
		autoplay:false,
		items:3,
		loop:true,
		margin:0,
		nav:true,
		dots:true,
		autoplaySpeed: 1000,
		navSpeed: 1000,
		paginationSpeed: 1000,
		slideSpeed: 1000,
		navText: ['<div class="glyph-icon flaticon-left-arrow"></div>', '<div class="glyph-icon flaticon-right-arrow"></div>'],
		responsive:{
			0:{
				items:1	
			},
			991:{
				items:3
			}
		}
	})
	
	/*  testimonial four function by = owl.carousel.js */
	jQuery('.widget-project-box').owlCarousel({
		loop:true,
		autoplay:true,
		margin:0,
		nav:false,
		dots: true,
		navText: ['<i class="flaticon-left-arrow"></i>', '<i class="flaticon-right-arrow"></i>'],
		responsive:{
			0:{
				items:1
			},
			991:{
				items:1
			}
		}
	})
	
});
/* Document .ready END */