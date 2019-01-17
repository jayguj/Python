import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { DataService } from '../data.service';
@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {


  signinObject = {
    userName:'',
    password: ''
  }

  messageForm: FormGroup;
  submitted = false;
  success = false;

  constructor(private formBuilder: FormBuilder,
    private dataService:DataService

  ) {
    this.messageForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    })
  }

  onSubmit() {
    this.submitted = true;
    console.log(this.signinObject)

    this.dataService.loginUser(this.signinObject.userName, this.signinObject.password)
      .subscribe( (data)=>{
        console.log("Response: ",data);
      })

    if (this.messageForm.invalid) {
      return;
    }

    this.success = true;
  }

  ngOnInit() {
  }

}
