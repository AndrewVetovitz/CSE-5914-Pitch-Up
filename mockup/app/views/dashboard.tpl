% rebase('base.tpl', title='My Pitch Summary')

<div> 
  <h2>My Recordings</h2>
  <table id="queue_table" class="table table-hover" style="margin-top: 25px;">
    <thead>
      <tr>
        <th scope="col"></th>
        <th scope="col">Recording Name</th>
        <th scope="col">Created On</th>
        <th scope="col">Score</th>
      </tr>
    </thead>
    <tbody>
      <tr class="table-row" style="cursor: pointer;">
          <td><input type="checkbox"></td>
          <td onclick="location.href='/recording_summary/1';">Recording #1</td>
          <td onclick="location.href='/recording_summary/1';">09-12-2018 08:30 PM</td>
          <td onclick="location.href='/recording_summary/1';">78%</td>
      </tr>
      <tr class="table-row" style="cursor: pointer;">
        <td><input type="checkbox"></td>
        <td onclick="location.href='/recording_summary/2';">Recording #2</td>
        <td onclick="location.href='/recording_summary/2';">09-12-2018 07:30 PM</td>
        <td onclick="location.href='/recording_summary/2';">70%</td>
      </tr>
      <tr class="table-row" style="cursor: pointer;">
        <td><input type="checkbox"></td>
        <td onclick="location.href='/recording_summary/3';">Recording #3</td>
        <td onclick="location.href='/recording_summary/3';">09-12-2018 08:30 PM</td>
        <td onclick="location.href='/recording_summary/3';">20%</td>
      </tr>
    </tbody>
  </table>

</div>

<hr class="mb-5"/>

<div>
  <h2>My Stats</h2>
    <div class="row mb-3">
          <div class="col-xl-4 col-sm-12 py-2">
              <div class="card bg-success text-white h-100 w-30">
                  <div class="card-body bg-success">
                      <div class="rotate">
                          <i class="fa fa-user fa-4x"></i>
                      </div>
                      <h6 class="text-uppercase">Recordings</h6>
                      <h1 class="display-4">3</h1>
                  </div>
              </div>
          </div>
          <div class="col-xl-4 col-sm-12 py-2">
              <div class="card text-white bg-danger h-100 w-30">
                  <div class="card-body bg-danger">
                      <div class="rotate">
                          <i class="fa fa-list fa-4x"></i>
                      </div>
                      <h6 class="text-uppercase">Total Time</h6>
                      <h1 class="display-4">3:15</h1>
                  </div>
              </div>
          </div>
          <div class="col-xl-4 col-sm-12 py-2">
              <div class="card text-white bg-info h-100 w-30">
                  <div class="card-body bg-info">
                      <div class="rotate">
                          <i class="fa fa-twitter fa-4x"></i>
                      </div>
                      <h6 class="text-uppercase">Average Score</h6>
                      <h1 class="display-4">58</h1>
                  </div>
              </div>
          </div>
      </div>

  <div class="mb-5">
    <canvas id="line-chart" width="500" height="200"></canvas>
  </div>
  
</div>

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