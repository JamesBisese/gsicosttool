# Generated by Django 2.2.6 on 2020-01-25 20:42

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArealFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stormwater_management_feature_area', models.IntegerField(blank=True, default=0, null=True, verbose_name='Stormwater Management Feature Area')),
                ('stormwater_management_feature_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name='Stormwater Management Feature Checked')),
                ('amenity_plaza_area', models.IntegerField(blank=True, default=0, null=True, verbose_name='Amenity Areas/Urban Plaza Area')),
                ('amenity_plaza_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name='Amenity Areas/Urban Plaza Checked')),
                ('protective_yard_area', models.IntegerField(blank=True, default=0, null=True, verbose_name='Protective Yards Area')),
                ('protective_yard_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name='Protective Yards Checked')),
                ('parking_island_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name=' Checked')),
                ('parking_island_area', models.IntegerField(blank=True, default=0, null=True, verbose_name=' Area')),
                ('building_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name=' Checked')),
                ('building_area', models.IntegerField(blank=True, default=0, null=True, verbose_name=' Area')),
                ('drive_thru_facility_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name=' Checked')),
                ('drive_thru_facility_area', models.IntegerField(blank=True, default=0, null=True, verbose_name=' Area')),
                ('landscape_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name=' Checked')),
                ('landscape_area', models.IntegerField(blank=True, default=0, null=True, verbose_name=' Area')),
                ('sidewalk_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name=' Checked')),
                ('sidewalk_area', models.IntegerField(blank=True, default=0, null=True, verbose_name=' Area')),
                ('street_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name=' Checked')),
                ('street_area', models.IntegerField(blank=True, default=0, null=True, verbose_name=' Area')),
                ('median_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name=' Checked')),
                ('median_area', models.IntegerField(blank=True, default=0, null=True, verbose_name=' Area')),
                ('parking_lot_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name=' Checked')),
                ('parking_lot_area', models.IntegerField(blank=True, default=0, null=True, verbose_name=' Area')),
                ('driveway_and_alley_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name=' Checked')),
                ('driveway_and_alley_area', models.IntegerField(blank=True, default=0, null=True, verbose_name=' Area')),
            ],
        ),
        migrations.CreateModel(
            name='ConventionalStructures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stormwater_wetland_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name='Stormwater Wetland Checked')),
                ('stormwater_wetland_area', models.IntegerField(blank=True, default=0, null=True, verbose_name='Stormwater Wetland Area')),
                ('stormwater_wetland_first_year_costs_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('stormwater_wetland_first_year_costs', djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0'), default_currency='USD', max_digits=11, null=True, verbose_name='1st year maintenance costs')),
                ('pond_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('pond_area', models.IntegerField(blank=True, default=0, null=True)),
                ('rooftop_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('rooftop_area', models.IntegerField(blank=True, default=0, null=True)),
                ('lawn_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('lawn_area', models.IntegerField(blank=True, default=0, null=True)),
                ('landscaping_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('landscaping_area', models.IntegerField(blank=True, default=0, null=True)),
                ('trench_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('trench_area', models.IntegerField(blank=True, default=0, null=True)),
                ('concrete_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('concrete_area', models.IntegerField(blank=True, default=0, null=True)),
                ('asphalt_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('asphalt_area', models.IntegerField(blank=True, default=0, null=True)),
                ('curb_and_gutter_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('curb_and_gutter_area', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CostItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=50, unique=True)),
                ('name', models.CharField(default=None, max_length=50, unique=True)),
                ('sort_nu', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Sort Number')),
                ('units', models.CharField(default=None, max_length=12)),
                ('help_text', models.CharField(default='TBD', max_length=1000)),
            ],
            options={
                'ordering': ['sort_nu'],
            },
        ),
        migrations.CreateModel(
            name='NonConventionalStructures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swale_area', models.IntegerField(blank=True, default=0, null=True, verbose_name='Swale Area')),
                ('swale_checkbox', models.BooleanField(blank=True, default=False, null=True, verbose_name='Swale Checked')),
                ('rain_harvesting_device_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('rain_harvesting_device_area', models.IntegerField(blank=True, default=0, null=True)),
                ('bioretention_cell_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('bioretention_cell_area', models.IntegerField(blank=True, default=0, null=True)),
                ('filter_strip_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('filter_strip_area', models.IntegerField(blank=True, default=0, null=True)),
                ('green_roof_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('green_roof_area', models.IntegerField(blank=True, default=0, null=True)),
                ('planter_box_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('planter_box_area', models.IntegerField(blank=True, default=0, null=True)),
                ('porous_pavement_checkbox', models.BooleanField(blank=True, default=False, null=True)),
                ('porous_pavement_area', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(default=None, max_length=200, verbose_name='Project Title')),
                ('project_ownership', models.CharField(blank=True, choices=[('private', 'Private'), ('public', 'Public')], max_length=15, null=True, verbose_name='Project Organizer')),
                ('project_location', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Location of the project')),
                ('project_type', models.CharField(blank=True, choices=[('redevelopment', 'redevelopment project focused on additional new impervious area'), ('development', 'whole site (new development)'), ('voluntary_redevelopment', 'BMP retrofit to existing development only (voluntary redevelopment)')], max_length=25, null=True, verbose_name='Project Type')),
                ('project_purchase_information', models.CharField(blank=True, choices=[('to_be_purchased', 'Site property needs to be purchased by developer'), ('owned', 'Site property is owned by developer')], default=None, max_length=15, null=True, verbose_name='Purchase Information')),
                ('priority_watershed', models.CharField(blank=True, choices=[('please_name', 'Yes - please name'), ('no', 'No')], default=None, max_length=15, null=True, verbose_name='Priority Watershed')),
                ('project_area', models.CharField(default=None, max_length=15, verbose_name='Total Project Area (square feet)')),
                ('land_unit_cost_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('land_unit_cost', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('1'), default_currency='USD', max_digits=11, verbose_name='Cost per ft2 of Project site')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'unique_together': {('user', 'project_title')},
            },
        ),
        migrations.CreateModel(
            name='Structures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=100, unique=True)),
                ('name', models.CharField(default=None, max_length=100, unique=True)),
                ('classification', models.CharField(choices=[('conventional', 'Conventional'), ('nonconventional', 'Non-Conventional')], default=None, max_length=15)),
                ('sort_nu', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Sort Number')),
                ('units', models.CharField(default=None, max_length=12)),
                ('units_html', models.CharField(default=None, max_length=25)),
                ('help_text', models.CharField(default='TBD', max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Structures',
                'ordering': ['sort_nu'],
            },
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scenario_title', models.CharField(default=None, max_length=200, verbose_name='Scenario Name')),
                ('scenario_date', models.DateField(blank=True, default=None, null=True, verbose_name='Scenario Date')),
                ('pervious_area', models.IntegerField(blank=True, default=0, null=True)),
                ('impervious_area', models.IntegerField(blank=True, default=0, null=True)),
                ('nutrient_req_met', models.CharField(blank=True, choices=[('with_buy_down', 'With Nutrient Buy Down'), ('without_buy_down', 'Without Nutrient Buy Down'), ('unknown', 'Unknown')], default='unknown', max_length=25, null=True, verbose_name='Level of nutrient requirements met')),
                ('captures_90pct_storm', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'unknown')], default='unknown', max_length=25, null=True, verbose_name='Site captures the 90th percentile storm volume')),
                ('meets_peakflow_req', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'unknown')], default='unknown', max_length=25, null=True, verbose_name='Site meets peak flow requirements')),
                ('planning_and_design_factor', models.CharField(blank=True, default='', max_length=12, null=True, verbose_name='Planning and Design Factor (Multiplier)')),
                ('study_life', models.IntegerField(blank=True, default=0, null=True, verbose_name='Study Life(years)')),
                ('discount_rate', models.FloatField(blank=True, default=0, null=True, verbose_name='Discount Rate(DISC)')),
                ('counter', models.IntegerField(default=0, verbose_name='Integer Counter')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('areal_features', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scenario.ArealFeatures')),
                ('conventional_structures', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scenario.ConventionalStructures')),
                ('nonconventional_structures', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scenario.NonConventionalStructures')),
                ('project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='scenario.Project')),
            ],
            options={
                'verbose_name_plural': 'Scenarios',
                'unique_together': {('project', 'scenario_title')},
            },
        ),
        migrations.CreateModel(
            name='CostItemDefaultEquations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equation_tx', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Equation')),
                ('a_area', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Area (a)')),
                ('z_depth', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Depth (z)')),
                ('d_density', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Density (d)')),
                ('r_ratio', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Ratio (r)')),
                ('n_number', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Count (n)')),
                ('help_text', models.CharField(default='Help Text', max_length=1000)),
                ('costitem', models.OneToOneField(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='scenario.CostItem')),
            ],
            options={
                'verbose_name_plural': 'Cost Item Default Equations',
                'ordering': ['costitem__sort_nu'],
            },
        ),
        migrations.CreateModel(
            name='CostItemDefaultCosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rsmeans_va_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('rsmeans_va', djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='USD', max_digits=11, null=True, verbose_name='RSMeans unit cost')),
                ('db_25pct_va_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('db_25pct_va', djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='USD', max_digits=11, null=True, verbose_name='DB 25-percentile unit cost')),
                ('db_50pct_va_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('db_50pct_va', djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='USD', max_digits=11, null=True, verbose_name='DB Average unit cost')),
                ('db_75pct_va_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('db_75pct_va', djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='USD', max_digits=11, null=True, verbose_name='DB 75-percentile unit cost')),
                ('replacement_life', models.PositiveIntegerField(blank=True, default=40, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('o_and_m_pct', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('equation', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Construction Costs Equation ')),
                ('costitem', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='scenario.CostItem')),
            ],
            options={
                'verbose_name_plural': 'Cost Item Default Costs',
                'ordering': ['costitem__sort_nu'],
            },
        ),
        migrations.CreateModel(
            name='CostItemUserCosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_source', models.CharField(choices=[('rsmeans', 'Eng. Est.'), ('db_25_pct', 'DB - 25%'), ('db_50_pct', 'DB - 50%'), ('db_75_pct', 'DB - 75%')], default=None, max_length=24, verbose_name='Source of user_input_cost')),
                ('user_input_cost_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('user_input_cost', djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='USD', max_digits=11, null=True, verbose_name='User supplied unit cost')),
                ('base_year', models.PositiveIntegerField(blank=True, default=1990, null=True, validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2090)])),
                ('replacement_life', models.PositiveIntegerField(blank=True, default=40, null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(100)], verbose_name="Replacement Life ('R')")),
                ('o_and_m_pct', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Ongoing Operations and Maintenance Factor (%)')),
                ('first_year_maintenance_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('first_year_maintenance', djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='USD', max_digits=11, null=True, verbose_name='User supplied First Year Maintenance Cost')),
                ('costitem', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='scenario.CostItem')),
                ('scenario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cost_item_user_costs', to='scenario.Scenario')),
            ],
            options={
                'verbose_name_plural': 'Cost Item User Costs',
                'unique_together': {('scenario', 'costitem')},
            },
        ),
        migrations.CreateModel(
            name='CostItemUserAssumptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked', models.BooleanField(default=None, null=True, verbose_name='Checked in UI')),
                ('a_area', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Area (a)')),
                ('z_depth', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Depth (z)')),
                ('d_density', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Density (d)')),
                ('r_ratio', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Ratio (r)')),
                ('n_number', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Count (n)')),
                ('costitem', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='scenario.CostItem')),
                ('scenario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cost_item_user_assumptions', to='scenario.Scenario')),
                ('structure', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='scenario.Structures')),
            ],
            options={
                'verbose_name_plural': 'Structure Cost Item User Assumptions',
                'unique_together': {('scenario', 'structure', 'costitem')},
            },
        ),
        migrations.CreateModel(
            name='CostItemDefaultFactors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_area', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Area (a)')),
                ('z_depth', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Depth (z)')),
                ('d_density', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Density (d)')),
                ('n_number', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Count (n)')),
                ('costitem', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='scenario.CostItem')),
                ('structure', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='scenario.Structures')),
            ],
            options={
                'verbose_name_plural': 'Structure Cost Item Default Factors',
                'ordering': ['costitem__sort_nu'],
                'unique_together': {('structure', 'costitem')},
            },
        ),
    ]
