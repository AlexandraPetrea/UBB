#include "Sphere.h"


using namespace rt;

Intersection Sphere::getIntersection(const Line& line, float minDist, float maxDist) {
	Intersection in;

	// ADD CODE HERE

    return in;
}


const Vector Sphere::normal(const Vector& vec) const {
    Vector n = vec - _center;
    n.normalize();
    return n;
}
