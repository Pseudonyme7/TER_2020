import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { FormControl } from '@angular/forms';
import { UserService} from '../user.service';

@Component({ templateUrl: 'login.component.html' ,
    selector: 'recaptcha-demo',
    }
    )
export class LoginComponent implements OnInit {
    registerForm;
    submitted = false;

    constructor(
        private userService: UserService
    ) {

    }
    

    ngOnInit() {
        this.registerForm = ({
            firstName: '',
            lastName: '',
            username: '',
            password: '',
            email: '',
        });
    }

    // convenience getter for easy access to form fields
    get f() { return this.registerForm.controls; }

    onSubmit() {
        this.submitted = true;

   
        // stop here if form is invalid
        if (this.registerForm.invalid) {
            return;
        }


    }

    registerUser() {
      this.userService.registerUser(this.registerForm).subscribe(
  response => {
  
    alert('user' + this.registerForm.firstName + 'eh' + 'has been created ');
  }, error => console.log('error', error )
  );
    }

    public resolved(captchaResponse: string) {
        console.log(`Resolved captcha with response: ${captchaResponse}`);
    }
    public reactiveForm: FormGroup = new FormGroup({
        recaptchaReactive: new FormControl(null, Validators.required)
    });
}


