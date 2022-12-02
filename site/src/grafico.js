
let idCaixa = 1
let dados_cpu = []
let dados_memoria = []
let dados_disco = []
let momento = []
let pid = []
let usoCpuProcesso = []
let usoMemoriaProcesso = []

function pegardados(idCaixa) {
	fetch(`/data/obterdados/${idCaixa}`, { cache: 'no-store' }).then(function (response) {
		if (response.ok) {
			for (cont = 0; cont < response.length; cont++) {
				response.json().then(function (response) {
					dados_cpu.push(response[cont].cpuPorcentagem)
					dados_disco.push(response[cont].hdPorcentagem)
					dados_memoria.push(response[cont].ramPorcentagem)
					momento.push(response[cont].momento)
				});
			}

		} else {
			console.error("Falha ao Executar a API")
			return
		}
	});
}


function pegardadosJulia(idCaixa) {
	fetch(`/data/obterdadosJulia/${idCaixa}`, { cache: 'no-store' }).then(function (response) {
		if (response.ok) {
			for (cont = 0; cont < response.length; cont++) {
				response.json().then(function (response) {
					pid.push(response[cont].pid)
					usoCpuProcesso.push(response[cont].usoCpuProcesso)
					usoMemoriaProcesso.push(response[cont].usoMemoriaProcesso)
					momento.push(response[cont].momento)
				});
			}

		} else {
			console.error("Falha ao Executar a API")
			return
		}
	});
}



var ctx = document.getElementById('statisticsChart').getContext('2d');


for (cont = 0; response.length; cont++) {

	statisticsChart.labels = response.nome
}

var statisticsChart = new Chart(ctx, {
	type: 'line',
	data: {
		labels: ["14:00", "14:01", "14:02", "14:03", "14:04", "14:05", "14:06", "14:07", "14:08", "14:09", "14:10", "14:11"],
		datasets: [{
			label: "Cpu",
			borderColor: '#f3545d',
			pointBackgroundColor: 'rgba(243, 84, 93, 0.6)',
			pointRadius: 0,
			backgroundColor: 'rgba(243, 84, 93, 0.4)',
			legendColor: '#f3545d',
			fill: true,
			borderWidth: 2,
			data: ""
		}, {
			label: "Memória",
			borderColor: '#fdaf4b',
			pointBackgroundColor: 'rgba(253, 175, 75, 0.6)',
			pointRadius: 0,
			backgroundColor: 'rgba(253, 175, 75, 0.4)',
			legendColor: '#fdaf4b',
			fill: true,
			borderWidth: 2,
			data: [256, 230, 245, 287, 240, 250, 230, 295, 331, 431, 456, 521]
		}, {
			label: "Disco",
			borderColor: '#177dff',
			pointBackgroundColor: 'rgba(23, 125, 255, 0.6)',
			pointRadius: 0,
			backgroundColor: 'rgba(23, 125, 255, 0.4)',
			legendColor: '#177dff',
			fill: true,
			borderWidth: 2,
			data: [542, 480, 430, 550, 530, 453, 380, 434, 568, 610, 700, 900]
		}]
	},
	options: {
		responsive: true,
		maintainAspectRatio: false,
		legend: {
			display: false
		},
		tooltips: {
			bodySpacing: 4,
			mode: "nearest",
			intersect: 0,
			position: "nearest",
			xPadding: 10,
			yPadding: 10,
			caretPadding: 10
		},
		layout: {
			padding: { left: 5, right: 5, top: 15, bottom: 15 }
		},
		scales: {
			yAxes: [{
				ticks: {
					fontStyle: "500",
					beginAtZero: false,
					maxTicksLimit: 5,
					padding: 10
				},
				gridLines: {
					drawTicks: false,
					display: false
				}
			}],
			xAxes: [{
				gridLines: {
					zeroLineColor: "transparent"
				},
				ticks: {
					padding: 10,
					fontStyle: "500"
				}
			}]
		},
		legendCallback: function (chart) {
			var text = [];
			text.push('<ul class="' + chart.id + '-legend html-legend">');
			for (var i = 0; i < chart.data.datasets.length; i++) {
				text.push('<li><span style="background-color:' + chart.data.datasets[i].legendColor + '"></span>');
				if (chart.data.datasets[i].label) {
					text.push(chart.data.datasets[i].label);
				}
				text.push('</li>');
			}
			text.push('</ul>');
			return text.join('');
		}
	}
});



var myLegendContainer = document.getElementById("myChartLegend");

// generate HTML legend
myLegendContainer.innerHTML = statisticsChart.generateLegend();

// bind onClick event to all LI-tags of the legend
var legendItems = myLegendContainer.getElementsByTagName('li');
for (var i = 0; i < legendItems.length; i += 1) {
	legendItems[i].addEventListener("click", legendClickCallback, false);
}