import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  // users: object;
  homeObject={
    users:''
  }

  userList:Array<any>

  constructor(private data: DataService) { }

  ngOnInit() {
    this.data.getUsers(this.homeObject.users).subscribe(data => {
    console.log("Response:",data)
    this.userList = data;
  })
  }

}
