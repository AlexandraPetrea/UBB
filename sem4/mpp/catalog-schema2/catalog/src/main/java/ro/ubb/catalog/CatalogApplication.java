package ro.ubb.catalog;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class CatalogApplication {
	private static final Logger LOG = LoggerFactory.getLogger(CatalogApplication.class);


	public static void main(String[] args) {
		LOG.warn("sending hello world response...");
		SpringApplication.run(CatalogApplication.class, args);

	}



}

