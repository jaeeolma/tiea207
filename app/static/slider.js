/*$("#ex1").slider();
        $("#ex1").on("slide", function(slideEvt) {
            $("#ex1SliderVal").text(slideEvt.value);
        });*/
        
var slider = new Slider('#ex1', {
	formatter: function(value) {
		return 'Current value: ' + value;
	}
});