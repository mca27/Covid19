function DisplayChart(Active, recovered, deaths) {
    let options1=
        {
            title: {
                display: false,
                text: 'CAVID-19 Cases in India',
                fontSize: 15
            },
            legend: {
                display: true,
                position: 'right',
                labels: {
                    fontColor: '#111111'

                }
            },

            tooltips: {
                enabled: true,
            },
        };
    let options=
    {
        title: {
            display: false,
            text: 'CAVID-19 Cases in India',
            fontSize: 15
        },
        legend: {
            display: true,
            position: 'bottom',

            labels: {
                fontColor: '#111111'
            }

        },

        tooltips: {
            enabled: true,
        },
        scales:
        {
            yAxes: [{
                ticks: {
                    display:false,
                    beginAtZero:true,
                    fontColor:'#111111',
                },
                scaleLabel: {
                    display: true,
                    // labelString: 'probability'
                }
            }],
            xAxes: [{
                ticks: {
                    beginAtZero:true,
                    fontColor:'#111111',
                }
            }]
        }
    };
    let myChart=document.getElementById('myChart').getContext('2d')
    let massPopChart = new Chart(myChart, {
        type:'pie', //bar, hoizontalBar, pie, line, doughnut, radar, polarArea

        data:{
            labels: ['Active','Recovered', 'Deaths'],
            datasets: [{
                label: 'CAVID19',
                data:[Active, recovered, deaths],
                backgroundColor:['#8AC7DB', '#90ee90', '#ff726f'],
                hoverBorderWidth: 3,
            }]
        },
        options: options1
    })

    let barChart=document.getElementById('barChart').getContext('2d')
    let massBarChart = new Chart(barChart, {
        type:'bar', //bar, hoizontalBar, pie, line, doughnut, radar, polarArea
        data:{
            labels: ['Active','Recovered', 'Deaths'],
            datasets: [{
                label: 'CAVID19',
                data:[Active, recovered, deaths],
                backgroundColor:['#8AC7DB', '#90ee90', '#ff726f'],
                hoverBorderWidth: 3,
            }]
        },
        options: options
    })

}