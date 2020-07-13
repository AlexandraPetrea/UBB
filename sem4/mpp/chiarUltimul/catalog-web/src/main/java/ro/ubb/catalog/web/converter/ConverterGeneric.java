package ro.ubb.catalog.web.converter;

/**
 * Created by radu.
 */
public interface ConverterGeneric<Model, Dto> {
    Model convertDtoToModel(Dto dto);

    Dto convertModelToDto(Model model);
}
