import { CommonModule, NgFor } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-amis',
  standalone: true,
  imports: [NgFor, CommonModule],
  templateUrl: './amis.component.html',
  styleUrl: './amis.component.css'
})
export class AmisComponent {
  // à enlever plus tard
  amis = [
    {id: 1, name: "Yani"},
    {id: 2, name: "Hugo"},
    {id: 3, name: "Brice"},
    {id: 4, name: "Loan"},
  ]

  showProfile() {

  }
}
