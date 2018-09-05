<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
    <meta content="" name="description">
    <meta content="" name="author">
    <link href="favicon.ico" rel="icon"><!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
    <title>{{ title }}</title>
    <link href="/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/assets/css/custom/dashboard.css" rel="stylesheet">
    <link href="/assets/css/custom/app.css" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.js"></script>
</head>

<body>

    <!-- Top Header -->
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <a class="navbar-brand" href="#">
            <img src="/assets/img/pitchup-logo-flat-trans-sm.png" alt="PitchUp" style="max-height: 40px" />
        </a> <button aria-controls="navbarsExampleDefault" aria-expanded="false"
            aria-label="Toggle navigation" class="navbar-toggler d-lg-none" data-target="#navbarsExampleDefault"
            data-toggle="collapse" type="button"><span class="navbar-toggler-icon"></span></button>
    </nav>

    <div class="container-fluid">
        <div class="row">
            <nav class="col-sm-3 col-md-2 d-none d-sm-block bg-light sidebar">
                <ul class="nav nav-pills flex-column">
                    <li class="nav-item">
                        <a class="nav-link active" href="index.html">Sidebar Menu<span class="sr-only">(current)</span></a>
                    </li>
                </ul>
            </nav>

            <main class="col-sm-9 ml-sm-auto col-md-10 pt-3" role="main">
                <div class="row page-title-heading">
                    <div class="col-sm-10 col-xs-4 page-title-heading-title">
                        <h1>{{ title }}</h1>
                    </div>
                </div>

                <!-- Content -->
                {{ !base }}

            </main>
        </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>

    <script>
        window.jQuery || document.write('<script src="assets/js/vendor/jquery.min.js"><\/script>')
    </script>
    <script src="assets/js/vendor/popper.min.js"></script>
    <script src="dist/js/bootstrap.min.js"></script> <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="assets/js/ie10-viewport-bug-workaround.js"></script>

    <script type="text/javascript">
        new Chart(document.getElementById("line-chart"), {
            type: 'line',
            data: {
                labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                    "October", "November", "December"
                ],
                datasets: [{
                    data: [45, 55, 68, 75, 77, 79, 81, 84, 78, 87, 90, 92],
                    label: "John Smith",
                    borderColor: "#c45850",
                    fill: false
                }]
            },
            options: {
                legend: {
                    display: false
                },
                title: {
                    display: true,
                    text: 'John Smith Scores'
                },
                scales: {
                    yAxes: [{
                        display: true,
                        ticks: {
                            suggestedMin: 20
                        }
                    }]
                }
            }
        });
    </script>

</body>
</html>