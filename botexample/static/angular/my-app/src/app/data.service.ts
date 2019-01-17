import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  Url ="http://127.0.0.1:8000"

  constructor(private http: HttpClient) { }

  getUsers(users) {
    // return this.http.get('https://reqres.in/api/users')
    console.log("From Service:",users)
    let reqHeader={
      users:users
    }
    return this.http.get(this.Url)
  }


  loginUser(email,pass){
    console.log("From Service:", email ,pass)
    let reqHeader= {
      email : email,
      password: pass
    }
    return this.http.post(this.Url,reqHeader )


  }
}
