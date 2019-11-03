if($.cookie('message')!='hide'&&wgUserName)$('.sitemessage').fadeIn(750);else $('.sitemessage').hide();$('.sitemessage').find('p').append('<a href="#hide-message">[hide this message]</a>');$(document).on('click','a[href=#hide-message]',function(e){e.preventDefault();$('.sitemessage').fadeOut(750);$.cookie('message','hide',{expires:100})});;mw.loader.state({"site":"ready"});

/* cache key: 133099-basin:resourceloader:filter:minify-js:7:824b28e856eddd9c0708055270355805 */
