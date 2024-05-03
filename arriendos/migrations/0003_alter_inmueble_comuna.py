# Generated by Django 4.2 on 2024-05-02 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arriendos', '0002_alter_inmueble_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='comuna',
            field=models.CharField(choices=[('alhue', 'Alhué'), ('bup', 'Buin'), ('calera_de_tango', 'Calera de Tango'), ('cerrillos', 'Cerrillos'), ('cerro_navia', 'Cerro Navia'), ('colina', 'Colina'), ('conchali', 'Conchalí'), ('curacavi', 'Curacaví'), ('el_bosque', 'El Bosque'), ('el_monte', 'El Monte'), ('estacion_central', 'Estación Central'), ('huechuraba', 'Huechuraba'), ('independencia', 'Independencia'), ('isla_de_maipo', 'Isla de Maipo'), ('la_cisterna', 'La Cisterna'), ('la_florida', 'La Florida'), ('la_granja', 'La Granja'), ('la_pintana', 'La Pintana'), ('la_reina', 'La Reina'), ('lam_p', 'Lampa'), ('las_condes', 'Las Condes'), ('lo_barnechea', 'Lo Barnechea'), ('lo_espejo', 'Lo Espejo'), ('lo_prado', 'Lo Prado'), ('macul', 'Macul'), ('maipu', 'Maipú'), ('m_elp', 'Melipilla'), ('nunoa', 'Ñuñoa'), ('padre_hurtado', 'Padre Hurtado'), ('p_provi', 'Peñaflor'), ('penalolen', 'Peñalolén'), ('p_hied', 'Pirque'), ('pomaire', 'Puente Alto'), ('p_sure', 'Providencia'), ('p_gavia', 'Pudahuel'), ('q_p_sal', 'Quilicura'), ('qlq_p', 'Quinta Normal'), ('r_v_z', 'Recoleta'), ('l_g_a', 'Renca'), ('s_r_', 'San Bernardo'), ('s_joa', 'San Joaquín'), ('s_jos', 'San José de Maipo'), ('s_m_v', 'San Miguel'), ('s_p_p', 'San Pedro'), ('s_r_a', 'San Ramón'), ('s_mar', 'Santiago'), ('s_l_s', 'Talagante'), ('v_f', 'Til Til'), ('v_e_p', 'Vitacura')], max_length=50),
        ),
    ]
