import { Component } from '@angular/core';
import { TestService } from './test.service'

import { FormBuilder } from '@angular/forms';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent  {

  checkoutForm = this.fb.group({
    fname: null,
    lname: null,
  });

  constructor(
    private testServ: TestService,
    private fb: FormBuilder,
    ) { }


  onSubmit(): void{
    let datos = {
      full_name: this.checkoutForm.value.fname,
      nick_name: this.checkoutForm.value.lname,
    }
    if(!datos.full_name || !datos.nick_name) {
      alert('Llena el formulario completo');
    }
    else {
      this.testServ.postTest(datos).subscribe(
        success => {console.log(success)},
        error => {console.log(error)}
      )
      this.checkoutForm.reset();
      alert('Tus datos se han enviado');

    }

  }

}
