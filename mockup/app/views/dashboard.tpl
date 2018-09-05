% rebase('base.tpl', title='Dashboard')

<div class="col-sm-8" style="margin-top: 20px;">
  
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
          <td onclick="location.href='my_recording.html';">Recording #1</td>
          <td onclick="location.href='my_recording.html';">09-12-2018 08:30 PM</td>
          <td onclick="location.href='my_recording.html';">78%</td>
      </tr>
      <tr class="table-row" style="cursor: pointer;">
        <td><input type="checkbox"></td>
        <td onclick="location.href='my_recording.html';">Recording #2</td>
        <td onclick="location.href='my_recording.html';">09-12-2018 07:30 PM</td>
        <td onclick="location.href='my_recording.html';">70%</td>
      </tr>
      <tr class="table-row" style="cursor: pointer;">
        <td><input type="checkbox"></td>
        <td onclick="location.href='my_recording.html';">Recording #3</td>
        <td onclick="location.href='my_recording.html';">09-12-2018 08:30 PM</td>
        <td onclick="location.href='my_recording.html';">20%</td>
      </tr>
    </tbody>
  </table>

</div>

<div class="col-md-10">
  <h2>My Stats</h2>
  <div class="row mb-3">
          <div class="col-xl-2 col-sm-6 py-2">
              <div class="card bg-success text-white h-100">
                  <div class="card-body bg-success">
                      <div class="rotate">
                          <i class="fa fa-user fa-4x"></i>
                      </div>
                      <h6 class="text-uppercase">Recordings</h6>
                      <h1 class="display-4">3</h1>
                  </div>
              </div>
          </div>
          <div class="col-xl-2 col-sm-6 py-2">
              <div class="card text-white bg-danger h-100">
                  <div class="card-body bg-danger">
                      <div class="rotate">
                          <i class="fa fa-list fa-4x"></i>
                      </div>
                      <h6 class="text-uppercase">Total Time</h6>
                      <h1 class="display-4">3:15</h1>
                  </div>
              </div>
          </div>
          <div class="col-xl-2 col-sm-6 py-2">
              <div class="card text-white bg-info h-100">
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

  <div style="width: 50%; margin-bottom: 75px;">
    <canvas id="line-chart" width="500" height="300"></canvas>
  </div>
  
</div>
