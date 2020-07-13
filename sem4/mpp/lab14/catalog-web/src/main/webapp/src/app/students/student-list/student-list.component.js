"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var core_1 = require('@angular/core');
var StudentListComponent = (function () {
    function StudentListComponent(studentService, router) {
        this.studentService = studentService;
        this.router = router;
    }
    StudentListComponent.prototype.ngOnInit = function () {
        this.getStudents();
    };
    StudentListComponent.prototype.getStudents = function () {
        var _this = this;
        this.studentService.getStudents()
            .subscribe(function (students) { return _this.students = students; }, function (error) { return _this.errorMessage = error; });
    };
    StudentListComponent.prototype.onSelect = function (student) {
        this.selectedStudent = student;
    };
    StudentListComponent.prototype.gotoDetail = function () {
        this.router.navigate(['/student/detail', this.selectedStudent.id]);
    };
    StudentListComponent = __decorate([
        core_1.Component({
            moduleId: module.id,
            selector: 'ubb-student-list',
            templateUrl: './student-list.component.html',
            styleUrls: ['./student-list.component.css'],
        })
    ], StudentListComponent);
    return StudentListComponent;
}());
exports.StudentListComponent = StudentListComponent;
