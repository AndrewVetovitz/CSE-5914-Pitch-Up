% rebase('base.tpl', title='')


<div class="row" style="text-align: center">

    <div class="col-sm-12">

        <div id="ai" class="well" style="background: url(/assets/img/loader-white.gif) no-repeat center center; height: 500px; width: 100%; display: none; box-shadow: inset 0 0 20px 20px white;">
        </div>
        <h2 id="statustext" class="text-center text-info" style="display: none"></h2>
        <div id="results" style="display: none;">
            <a class="btn btn-primary btn-lg" href="/recording_summary/3">See Results</a>
        </div>
    
    </div>

</div>

<script>
$(document).ready(function() {

        var i = 0;
        var status_text = [
            'Beginning analysis...',
            'Almost there...',
            'Analysis complete.'
        ];
        var status_container = $('#statustext');

        $('#ai').fadeIn(3000);
            
        var status_update = setInterval(function(){

            status_container.text(status_text[i]).fadeIn(1000).delay(1000);

            i++;

            if (i == status_text.length) {
                clearInterval(status_update);
                $("#results").delay(3000).fadeIn(1000);
                
            } else {
                status_container.fadeOut(1000);
            }

        }, 3000);

        
});
</script>
