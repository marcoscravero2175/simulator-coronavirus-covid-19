// HistogramModule.js
		var HistogramModule = function(bins, canvas_width, canvas_height) {
		    var canvas_tag = "<canvas width='" + canvas_width + "' height='" + canvas_height + "' ";
		    canvas_tag += "style='border:1px dotted'></canvas>";
		    var canvas = $(canvas_tag)[0];
		    $("body").append(canvas);
		    var context = canvas.getContext("2d");

		bins = [
			"Susceptibles",
			"Infectados",
			"Inmunizados",
			"Muertos",
			]

        dataNew = [
			10,
			23,
			10,
			23,
			]

		var datos = {
			type: "pie",
			data : {
				datasets :[{
					data : dataNew,
					backgroundColor: [
						'rgba(255, 206, 86, 1)',
						'rgba(255, 99, 132, 0.3)',
						'rgba(54, 162, 235, 1)',
						'rgba(255, 99, 132, 1)',
					],
				}],
				labels : bins
			},
			options : {
				responsive : true,
			}
		};



	        var chart = new Chart(context, datos);


	        for (var i in dataNew) {
                    //alert(chart.data.datasets[0].data[i])
	                chart.data.datasets[0].data[i] = 4;
            }
	        chart.update();


	        this.render = function(data) {
        	   for (var i in data) {
                    //alert(chart.data.datasets[0].data[i])
	                chart.data.datasets[0].data[i] = data[i];
               }
      	       chart.update();
    	     };

		    
	     };

	     //alert("c1")
	     //var hist1 = new HistogramModule(10, 200, 500)
