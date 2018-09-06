% rebase('base.tpl', title='Recording Summary')

<h2>Recording {{id}} results</h2>
<br/>

<div>
    <h2>Audio Playback</h2>
    <div style="margin-top: 15px;">
        <audio controls>
            %if id == '1':
                <source src="/assets/recording1.mp3" type="audio/mpeg">
            %elif id == '2':
                <source src="/assets/recording2.mp3" type="audio/mpeg">
            %elif id == '3':
                <source src="/assets/recording3.mp3" type="audio/mpeg">
            %end
            Your browser does not support the audio element.
        </audio>
    </div>
</div>
<br/>

<div>
    <h2>Text from speech</h2>
    %if id == '1':
        Hi. My name is Andrew and this is um my interview. I just wanted to say thank you for
        your time. I am looking for a software job and um wanted to get... To do some fun work.
        Thank you again. Bye.
    %elif id == '2':
        Hi. My name is Andrew Vetovitz and this is um my interview. I just wanted to say thank you for
        your time. I am looking for a software engineering job. I really like your company.
        Thank you again. Bye.
    %elif id == '3':
        Hi. My name is Andrew Vetovitz. I just wanted to say thank you for your time. 
        I am looking for a software engineering job. I find the work that your company 
        does to be very interesting. It looks challenging and is something that can help me 
        grow as well as give your company value.
    %end

    <br/>
    <br/>

    <h2>Positives</h2>
    %if id == '1':
        Decent length.
    %elif id == '2':
        Good length. <br/>
        Few mistakes.
    %elif id == '3':
        Strong vocabulary.  <br/>
        Good length. <br/>
        No basic mistakes.
    %end

    <br/>
    <br/>

    <h2>Basic Mistakes</h2>
    %if id == '1':
        ums: 2 <br/>
        pauses: 1
    %elif id == '2':
        ums: 1 <br/>
        pauses: 0
    %elif id == '3':
        ums: 0 <br/>
        pauses: 0
    %end

    <br/>
    <br/>

    <h2>Other info</h2>
    %if id == '1':
        Length: 60 seconds<br/>
        Words: 42
    %elif id == '2':
        Length: 75 seconds<br/>
        Words: 38
    %elif id == '3':
        Length: 90 seconds<br/>
        Words: 54
    %end

    <br/>
    <br/>

    <h2>Score: 
    %if id == '1':
        56
    %elif id == '2':
        82
    %elif id == '3':
        88
    %end
    </h2>
</div>