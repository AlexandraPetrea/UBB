package ro.ubb.catalog.core.service;

import ro.ubb.catalog.core.model.User;

/**
 * Created by radu.
 */
public interface UserService {

    User getUserByUserName(String userName);
}
