% rebase('base.tpl', title='Create a new Pitch')

<form>

    <div class="form-group row mb-5">
        <label for="inputEmail3" class="col-sm-2 col-form-label">Pitch Name</label>
        <div class="col-sm-10">
            <input type="email" class="form-control" id="inputEmail3" placeholder="Name your pitch something memorable...">
        </div>
    </div>

    <hr />
    <h5>Documents</h5>
    <h6>Upload some documents to help PitchUp understand your topic!</h6>

    <div class="form-group row mb-5">
        <label for="exampleFormControlFile1" class="col-sm-2 col-form-label">Document 1</label>
        <div class="col-sm-10">
            <input type="file" class="form-control-file" id="exampleFormControlFile1">
        </div>
    </div>

    <div class="form-group row">
        <label for="exampleFormControlFile1" class="col-sm-2 col-form-label">Document 2</label>
        <div class="col-sm-10">
            <input type="file" class="form-control-file" id="exampleFormControlFile1">
        </div>
    </div>

    <div class="form-group row">
        <label for="exampleFormControlFile1" class="col-sm-2 col-form-label">Document 3</label>
        <div class="col-sm-10">
            <input type="file" class="form-control-file" id="exampleFormControlFile1">
        </div>
    </div>

    <br/>

    <div class="form-group row">
        <div class="col-sm-10">
            <a href="/dashboard" class="btn btn-primary">Create this Pitch</a>
        </div>
    </div>

</form>