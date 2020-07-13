"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var core_1 = require('@angular/core');
var http_1 = require("@angular/http");
var rxjs_1 = require("rxjs");
require('rxjs/add/operator/catch');
require('rxjs/add/operator/map');
var StudentService = (function () {
    function StudentService(http) {
        this.http = http;
        this.studentsUrl = 'http://localhost:8080/api/students';
    }
    StudentService.prototype.getStudents = function () {
        return this.http.get(this.studentsUrl)
            .map(this.extractData)
            .catch(this.handleError);
    };
    StudentService.prototype.extractData = function (res) {
        var body = res.json();
        return body.students || {};
    };
    StudentService.prototype.handleError = function (error) {
        var errMsg;
        if (error instanceof http_1.Response) {
            var body = error.json() || '';
            var err = body.error || JSON.stringify(body);
            errMsg = error.status + " - " + (error.statusText || '') + " " + err;
        }
        else {
            errMsg = error.message ? error.message : error.toString();
        }
        console.error(errMsg);
        return rxjs_1.Observable.throw(errMsg);
    };
    StudentService.prototype.getStudent = function (id) {
        return this.getStudents()
            .map(function (students) { return students.find(function (student) { return student.id === id; }); });
    };
    StudentService = __decorate([
        core_1.Injectable()
    ], StudentService);
    return StudentService;
}());
exports.StudentService = StudentService;
