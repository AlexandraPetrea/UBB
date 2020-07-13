import {Component, Input} from "@angular/core";
import {Location} from '@angular/common';

import {Student} from "../shared/student.model";
import {StudentService} from "../shared/student.service";


@Component({
  moduleId: module.id,
  selector: 'ubb-student-new',
  templateUrl: './student-new.component.html',
  styleUrls: ['./student-new.component.css'],
})
export class StudentNewComponent {

  constructor(private studentService: StudentService,
              private location: Location) {
  }

  goBack(): void {
    this.location.back();
  }

  save(serialNumber, name, groupNumber): void {
    if (!this.isValid(serialNumber, name, groupNumber)) {
      console.log("all fields are required ");
      alert("all fields are required; groupNumber has to be an int");
      return;
    }
    this.studentService.create(serialNumber, name, groupNumber)
      .subscribe(_ => this.goBack());
  }

  private isValid(serialNumber, name, groupNumber) {
    if (!serialNumber || !name || !groupNumber) {
      console.log("all fields are required");
      return false;
    }
    if (!Number.isInteger(Number(groupNumber))) {
      console.log("groupNumber has to be an int");
      return false;
    }
    //TODO other validations
    return true;
  }
}
