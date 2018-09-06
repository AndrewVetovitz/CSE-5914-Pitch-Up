% rebase('base.tpl', title='Recording Summary')

<h2>Recording {{id}} results</h2>
<br/>

<div>
    <h2>Audio Playback</h2>
    <div style="margin-top: 15px;">
        <audio controls>
            <source src="music.mp3" type="audio/mpeg">
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
        Hi. My name is Andrew Vetovitz and this is my interview. I just wanted to say thank you for
        your time. I am looking for a software engineering job. I really like your company.
        Thank you again. Bye.
    %elif id == '3':
        Hi. My name is Andrew Vetovitz. I just wanted to say thank you for
        your time. I am looking for a software engineering job. I find the work that your company to be
        very interesting. It looks challenging is something that can help me grow as well as give your
        company value. Thank you again for your time.
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
        Words: 58
    %end
</div>