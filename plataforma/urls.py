from django.urls import path, include
from . import views
from .views import CustomPasswordResetView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name='Index'),
    path('ListaProyectos/', views.ListaProyectos, name='ListaProyectos'),
    path('listaArchivoProyectos/', views.ListaArchivoProyectos, name='ListaArchivoProyectos'),
    path('crearProyecto/',views.crearProyecto,name="crearProyecto"),
    path('unirteProyecto/',views.UnirteProyecto,name="unirteProyecto"),
    path ('ListaAlumnosProfesores/<str:codigo>', views.ListaAlumnosProfesores,name="ListaAlumnosProfesores"),
    path('IntroduccionCoil/<str:codigo>', views.IntroduccionCoil,name="IntroduccionCoil"),
    path('Foro/<str:codigo>', views.ProyectoDetail,name="ProyectoDetail"),
    path('ListaActividadesPorFases/', views.ListaActividadesPorFases, name="ListaActividadesPorFases"),
    path('ConfiguracionProyecto/<str:codigo>',views.ConfiguracionProyecto, name="ConfiguracionProyecto"),
    path('SeguimientoActividad/<str:codigo>',views.SeguimientoActividad,name='SeguimientoActividad'),
    path('ViAlMateriales/<int:material_id>/', views.ViAlMateriales, name='ViAlMateriales'),
    path('AgregarMaterial/', views.AgregarMaterial, name='AgregarMaterial'),
    path('MaterialComentarios/<int:id_material>', views.MaterialComentarios, name='MaterialComentarios'),
    path('comentarioPrivMaterial/<int:id_material>/<int:id_alumno>',views.comentarioPrivMaterial,name="comentarioPrivMaterial"),

        #APARTADO DE ACTIVIDADES
    path('ViAlActividades/<int:actividad_id>/', views.ViAlActividades, name='ViAlActividades'),
    path('AgregarActividad/', views.AgregarActividad, name='AgregarActividad'),
    path('ActividadComentarios/<int:id_actividad>', views.ActividadComentarios, name='ActividadComentarios'),
    path('comentarioPrivActividad/<int:id_actividad>/<int:id_alumno>',views.comentarioPrivActividad,name="comentarioPrivActividad"),
    path('subirActividad/<int:id_actividad_parm>',views.subirActividad,name="subirActividad"),

    #PATH DEL SEGUIMIENTO DE LAS ACTIVIDADES DEL MALUMNO
    path('SeguimientoAct/<str:codigo>/<int:id_alumno>',views.SeguimientoAct,name="SeguimientoAct"),
    path('calificarActividad/<int:id_entrega>/<int:id_alumno>/<str:codigo>',views.calificarActividad,name="calificarActividad"),
    path('anularCalificacionActividad/<int:id_entrega>/<int:id_alumno>/<str:codigo>',views.anularCalificacionActividad,name="anularCalificacionActividad"),

    # EDITAR Y ELIMINAR ACTIVIDADES
    path('editarActividad/<int:id_actividad>',views.editarActividad,name="editarActividad"),
    path('eliminar_actividad/<int:id_actividad>',views.eliminar_actividad,name="eliminar_actividad"),
   
    # EDITAR Y ELIMINAR MATERIALES
    path('editarMaterial/<int:material_id>',views.editarMaterial,name="editarMaterial"),
    path('eliminar_material/<int:material_id>',views.eliminar_material,name="eliminar_material"),

    path('Registro/', views.Registro, name='Registro'),
    path('Login/', views.Login, name='Login'),
    path('Home/', views.Home, name="Home"),
    path('Logout/', views.logout_view, name='logout'),
    path('verificationcode/', views.verify_code, name='verify_code'),
    path('EditarUsuario/', views.EditarUsuario, name='editar_usuario'),
    
    path('guardar_usuario/', views.guardar_usuario, name='guardar_usuario'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
    
    
    
    path('registro_alumno/', views.RegistroAlumno, name='registro_alumno'),
    path('save_other_university/', views.save_other_university, name='save_other_university'),
    path('registro_profesor/', views.RegistroProfesor, name='registro_profesor'),
    path('ProfesorDatosPersonales/', views.ProfesorDatosPersonales, name='ProfesorDatosPersonales'),
    path('EditDatosProfesor/<str:codigo>', views.EditDatosProfesor, name="EditDatosProfesor"),
    
    
    path('Validatecredentials/', views.validate_credentials, name='validate_credentials'),
    path('Checkusername/', views.check_username, name='check_username'),
    path('fasesCoil/<str:codigo>',views.indexFases,name="FasesCoil"),
    path('fasesCoil/<str:codigo>/<int:idFase>',views.Fase1,name="Fase"),

    path('error/<str:error>',views.Error,name="Error"),
    path('Proyecto/<str:codigo>',views.UnirteProyectoPage, name="EntrarProyecto"),
    path('AgregarUsuarioProyecto/<int:proyecto>/<str:codigo>',views.AgregarUsuarioProyecto, name="AgregarUsuarioProyecto"),
    path('EditarProyecto/<int:proyecto>/<str:codigo>',views.editarProyecto, name="EditarProyecto"),
    path('ZoomProyecto/<int:proyecto>/<str:codigo>',views.zoomProyecto, name="ZoomProyecto"),
    path('ArchivarProyecto/<int:proyecto>/<str:codigo>',views.ArchivarProyecto, name="ArchivarProyecto"),
    path('ReactivarProyecto/<int:proyecto>/<str:codigo>',views.ReactivarProyecto, name="ReactivarProyecto"),
    path('CrearAnucio/<int:proyecto>/<str:codigo>',views.PublicarComentario,name="PublicarComentario"),
    path('ComentarAnucio/<int:publicacion>/<str:codigo>',views.ComentarPublicacion,name="ComentarPublicacion"),
    path('EliminarComentarioAnucio/<int:id_coment>/<str:codigo>',views.eliminarComentario,name="eliminarComentario"),
    path('EliminarAnucio/<int:id_anuncio>/<str:codigo>',views.eliminarAnuncio,name="eliminarAnuncio"),
    path('EditarComentarioAnucio/<int:id_coment>/<str:codigo>',views.editarComentario,name="editarComentario"),
    # path('articulos/',views.articulos,name="articulos"),
    # path('articulo/',views.arcticulo,name="articulo"),
    path('invitarProyecto/<str:codigo>',views.invitarProyecto,name="invitarProyecto"),
    path('expulsarAlumno/<int:id_alumno>/<str:codigo>',views.expulsarAlumno,name="expulsarAlumno"),
    path('expulsarProfesor/<int:id_profesor>/<str:codigo>',views.expulsarProfesor,name="expulsarProfesor"),
    path('adminProyecto/<int:id_profesor>/<str:codigo>',views.adminProyecto,name="adminProyecto"),
    path('editarPost/<int:id_anuncio>/<str:codigo>',views.editarPost,name="editarPost"),
    path('editarAnuncio/<int:id_anuncio>/<str:codigo>',views.editarPostVista,name="editarPostVista")
]